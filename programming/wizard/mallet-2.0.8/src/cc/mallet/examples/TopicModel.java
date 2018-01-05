package cc.mallet.examples;

import cc.mallet.util.*;
import cc.mallet.types.*;
import cc.mallet.pipe.*;
import cc.mallet.pipe.iterator.*;
import cc.mallet.topics.*;

import java.util.*;
import java.util.regex.*;
import java.io.*;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
/**
 * Class combining mallet topic modelling + bsi compendium
 * @author Raphael
 *
 */
public class TopicModel {

	/**
	 * Main method (starting point)
	 * @param args
	 */
	public static void main(String[] args) {
		String result = null;

		//Get all files from folder passed as argument
		File[] files = new File(args[0]).listFiles();

		//Read in the CSV file which file already have been processed
		List<File> unprocessedFiles = null;
		try {
			unprocessedFiles = getUnprocessedFiles(args, files);
		} catch (IOException e1) {
			e1.printStackTrace();
		}

		//For each unprocessed file
		for(File f : unprocessedFiles)  {
			//Check if it's a directory and note a .DS_Store (had local problem with these, could be removed once on the server)
			if(!f.isDirectory() && (!f.getName().equals(".DS_Store"))) {
				System.out.println("File: " + f.getAbsolutePath());
				result = null;
				try {
					//Get topics of this file
					result = getTopic(f);
				}
				catch (Exception e) {
					System.out.println("error with file:" + f.getName());
					e.printStackTrace();
				}
				//Append results to CSV result file
				if(result != null) {
					result = f.getAbsolutePath() + ";" + result;
					List<String> lines = Arrays.asList(result);
					Path file = Paths.get(args[0] + "/0/results.csv");
					try {
						Files.write(file, lines, Charset.forName("UTF-8"), StandardOpenOption.APPEND);
					} catch (IOException e) {
						e.printStackTrace();
					}
				}
			}
		}
	}

	private static List<File> getUnprocessedFiles(String[] args, File[] files) throws IOException  {

		List<File> unprocessedFiles = new ArrayList<>();
		List<String> processedFiles = new ArrayList<>();

		System.out.println("reading allready processed files...");
		for(String s : Files.readAllLines(new File(args[0] + "0/results.csv").toPath()))
		{
			processedFiles.add(s.split(";")[0]);
		}

		System.out.println(processedFiles.size() + " files were already processed...");

		for(File f : files) {
			if(!processedFiles.contains(f.getAbsolutePath())) {
				unprocessedFiles.add(f);
			}
		}
		System.out.println(unprocessedFiles.size() + " files are remaining...");
		return unprocessedFiles;
	}

	public static String getTopic(File f)  throws Exception {
		// Begin by importing documents from text to feature sequences
		String ret = null;

		ArrayList<Pipe> pipeList = new ArrayList<Pipe>();

		// Pipes: lowercase, tokenize, remove stopwords, map to features
		pipeList.add( new CharSequenceLowercase() );
		pipeList.add( new CharSequence2TokenSequence(Pattern.compile("\\p{L}[\\p{L}\\p{P}]+\\p{L}")) );
		pipeList.add( new TokenSequenceRemoveStopwords(new File("stoplists/en.txt"), "UTF-8", false, false, false) );
		pipeList.add( new TokenSequence2FeatureSequence() );

		InstanceList instances = new InstanceList (new SerialPipes(pipeList));

		Reader fileReader = new InputStreamReader(new FileInputStream(f), "UTF-8");
		instances.addThruPipe(new CsvIterator (fileReader, Pattern.compile("^(\\S*)[\\s,]*(\\S*)[\\s,]*(.*)$"),
				3, 2, 1)); // data, label, name fields

		// Create a model with 100 topics, alpha_t = 0.01, beta_w = 0.01
		//  Note that the first parameter is passed as the sum over topics, while
		//  the second is
		int numTopics = 100;
            ParallelTopicModel model = new ParallelTopicModel(numTopics, 1.0, 0.01);

		model.addInstances(instances);

		// Use two parallel samplers, which each look at one half the corpus and combine
		//  statistics after every iteration.
		model.setNumThreads(2);

		// Run the model for 50 iterations and stop (this is for testing only,
		//  for real applications, use 1000 to 2000 iterations)
		model.setNumIterations(500);
		model.estimate();

		// Show the words and topics in the first instance

		// The data alphabet maps word IDs to strings
		Alphabet dataAlphabet = instances.getDataAlphabet();

		FeatureSequence tokens = (FeatureSequence) model.getData().get(0).instance.getData();
		LabelSequence topics = model.getData().get(0).topicSequence;

		Formatter out = new Formatter(new StringBuilder(), Locale.US);
		for (int position = 0; position < tokens.getLength(); position++) {
			out.format("%s-%d ", dataAlphabet.lookupObject(tokens.getIndexAtPosition(position)), topics.getIndexAtPosition(position));
		}
		System.out.println(out);

		//  Estimate the topic distribution of the first instance,
		//  given the current Gibbs state.
		double[] topicDistribution = model.getTopicProbabilities(0);

		// Get an array of sorted sets of word ID/count pairs
		ArrayList<TreeSet<IDSorter>> topicSortedWords = model.getSortedWords();

		// Show top 5 words in topics with proportions for the first document
		for (int topic = 0; topic < numTopics; topic++) {
			if(topic > 0) {
				break;
			}
			Iterator<IDSorter> iterator = topicSortedWords.get(topic).iterator();

			out = new Formatter(new StringBuilder(), Locale.US);
			out.format("%d;%.3f;", topic, topicDistribution[topic]);
			int rank = 0;
			while (iterator.hasNext() && rank < 10) {
				IDSorter idCountPair = iterator.next();
				out.format("%s (%.0f) ", dataAlphabet.lookupObject(idCountPair.getID()), idCountPair.getWeight());
				rank++;
			}
			System.out.println(out);
			ret = out.toString();
		}

		// Create a new instance with high probability of topic 0
		StringBuilder topicZeroText = new StringBuilder();
		Iterator<IDSorter> iterator = topicSortedWords.get(0).iterator();

		int rank = 0;
		while (iterator.hasNext() && rank < 5) {
			IDSorter idCountPair = iterator.next();
			topicZeroText.append(dataAlphabet.lookupObject(idCountPair.getID()) + " ");
			rank++;
		}

		// Create a new instance named "test instance" with empty target and source fields.
		InstanceList testing = new InstanceList(instances.getPipe());
		testing.addThruPipe(new Instance(topicZeroText.toString(), null, "test instance", null));

		TopicInferencer inferencer = model.getInferencer();
		double[] testProbabilities = inferencer.getSampledDistribution(testing.get(0), 10, 1, 5);
		System.out.println("0\t" + testProbabilities[0]);

		return ret;
	}
}