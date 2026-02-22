import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
import os
from collections import defaultdict

"""
Provided Html Parser implementation. You should NOT modify it.
"""
class HtmlParser:
    def __init__(self, urls, edges):
        self.graph = {}
        for u in urls:
            self.graph[u] = []
        
        for edge in edges:
            from_idx = edge[0]
            to_idx = edge[1]
            self.graph[urls[from_idx]].append(urls[to_idx])

    def getUrls(self, url):
        try:
            time.sleep(0.01)  # Simulate network latency
        except:
            pass
        
        links = self.graph.get(url)
        if links is None:
            return []
        return links

class Solution:
    def __init__(self):
        self.visited = set()

    def sanitize(self, url):
        idx = url.find('#')
        if idx != -1:
            return url[:idx]
        return url
    
    def getHostName(self, url):
        start = url.find('://')
        start += 3
        end = url.find('/', start)
        return url[start:end]

    def crawl(self, startUrl, htmlParser):
        # TODO: Implement crawl logic.
        hostName = self.getHostName(startUrl)
        bfs = [startUrl]
        visited = {startUrl}
        with ThreadPoolExecutor(max_workers = 8) as executor:
            while bfs:
                futures = {executor.submit(htmlParser.getUrls, startUrl): startUrl for startUrl in bfs}
                next_bfs = []
                for future in as_completed(futures):
                    print("finished getUrl for: " + futures[future])
                    nextUrls = future.result()
                    for nextUrl in nextUrls:
                        if nextUrl not in visited and self.getHostName(nextUrl) == hostName:
                            visited.add(nextUrl)
                            next_bfs.append(nextUrl)
                bfs = next_bfs
        return list(set([self.sanitize(url) for url in visited]))

def main():
    test1()
    test2()
    test3()

def test1():
    print("===== Test 1 =====")

    urls = ["http://example.com/page1", "http://example.com/page2", "http://example.com/page3#sectionA",
            "http://example.net/page4#"]
    edges = [[0, 1], [0, 2], [1, 3], [2, 0]]
    startUrl = "http://example.com/page1"

    parser = HtmlParser(urls, edges)
    solution = Solution()
    result = solution.crawl(startUrl, parser)
    print(result)
    # Expected: ["http://example.com/page1", "http://example.com/page2", "http://example.com/page3"]

def test2():
    print("===== Test 2 =====")

    urls = ["http://news.yahoo.com/home", "http://news.google.com/top", "http://news.yahoo.com/news"]
    edges = [[1, 0], [0, 2]]
    startUrl = "http://news.google.com/top"

    parser = HtmlParser(urls, edges)
    solution = Solution()
    result = solution.crawl(startUrl, parser)
    print(result)
    # Expected: ["http://news.google.com/top"]

def test3():
    print("===== Test 3 =====")

    urls = ["http://site.com/a", "http://site.com/b#frag1", "http://site.com/b#frag2", 
    "http://site.com/c", "http://other.com/x", "http://site.com/d", "http://site.com/e#", 
    "http://site.com/f"]
    edges = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4], [3, 5], [5, 0], [5, 6], [6, 7], [7, 0]]
    startUrl = "http://site.com/a"

    parser = HtmlParser(urls, edges)
    solution = Solution()
    result = solution.crawl(startUrl, parser)
    print(result)
    # Expected: ["http://site.com/a", "http://site.com/b", "http://site.com/c",
    # "http://site.com/d", "http://site.com/e", "http://site.com/f"]

if __name__ == "__main__":
    main()
