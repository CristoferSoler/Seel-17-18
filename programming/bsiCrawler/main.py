from scrapy import cmdline

if __name__ == "__main__":
    #
    cmdline.execute("scrapy runspider crawli.py --nolog".split())
