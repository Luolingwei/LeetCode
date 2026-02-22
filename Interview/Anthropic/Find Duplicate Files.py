import hashlib
from io import BytesIO
from typing import List, Dict, Optional

#
# Node representing either a directory or file in the simulated file system
#
class FSNode:
    def __init__(self, isDir=None, content=None):
        if content is not None:
            self.isDir = False
            self.content = content
        else:
            self.isDir = isDir if isDir is not None else True
            if self.isDir:
                self.children = {}

#
# In-memory file system implementation
#
class FileSystem:
    def __init__(self):
        self.root = FSNode(True)

    # Add a file from string content
    def addFile(self, path: str, content: str):
        self.addFileBytes(path, content.encode())

    # Add a file from raw bytes
    def addFileBytes(self, path: str, content: bytes):
        parts = self.splitPath(path)
        curr = self.root

        for i in range(len(parts) - 1):
            part = parts[i]
            if part not in curr.children:
                curr.children[part] = FSNode(True)
            curr = curr.children[part]
        fileName = parts[len(parts) - 1]
        curr.children[fileName] = FSNode(content=content)

    def listFiles(self, path: str) -> List[str]:
        node = self.getNode(path)
        if node is None or not node.isDir:
            return []
        result = []
        prefix = path if path.endswith("/") else path + "/"
        for name in node.children.keys():
            result.append(prefix + name)
        return result

    def isDirectory(self, path: str) -> bool:
        node = self.getNode(path)
        return node is not None and node.isDir

    def getFileSize(self, path: str) -> int:
        node = self.getNode(path)
        if node is None or node.isDir:
            return 0
        return len(node.content)

    def openStream(self, path: str):
        node = self.getNode(path)
        if node is None or node.isDir:
            return BytesIO(b'')
        return BytesIO(node.content)

    def getNode(self, path: str) -> Optional[FSNode]:
        if path == "/":
            return self.root
        parts = self.splitPath(path)
        curr = self.root
        for part in parts:
            if curr is None or not curr.isDir or part not in curr.children:
                return None
            curr = curr.children[part]
        return curr

    def splitPath(self, path: str) -> List[str]:
        cleaned = path
        if cleaned.startswith("/"):
            cleaned = cleaned[1:]
        if cleaned.endswith("/"):
            cleaned = cleaned[:-1]
        if not cleaned:
            return []
        return cleaned.split("/")

class DuplicateFileFinder:
    def __init__(self, fs: FileSystem):
        self.fs = fs
        self.sizeMap = {}

    def findDuplicateFiles(self) -> List[List[str]]:
        self.searchNode(self.fs.root, "")
        res = []
        for size, paths in self.sizeMap.items():
            if len(paths) > 1:
                temHashMap = {}
                for path in paths:
                    curHash = self.computeHash(path)
                    temHashMap[curHash] = temHashMap.get(curHash, []) + [path]
                res += [p for p in temHashMap.values() if len(p) > 1]
        return res
    
    def searchNode(self, fsNode, curPath):
        for k, v in fsNode.children.items():
            newPath = curPath + "/" + k
            # Leaf node, record content
            if not v.isDir: 
                fileSize = self.fs.getFileSize(newPath)
                self.sizeMap[fileSize] = self.sizeMap.get(fileSize, []) + [newPath]
            # Middle node, recurive search
            else:
                self.searchNode(v, newPath)
        
    def computeHash(self, filePath, chunk_size = 4096):
        stream = self.fs.openStream(filePath)
        sha256 = hashlib.sha256()
        while True:
            chunk = stream.read(chunk_size)
            if not chunk:
                break
            sha256.update(chunk)
        return sha256.hexdigest()


class Solution:
    @staticmethod
    def main():
        Solution.test1()
        Solution.test2()
        Solution.test3()

    @staticmethod
    def test1():
        print("===== Test 1 =====")

        fs = FileSystem()
        fs.addFile("/a/x.txt", "hello world")
        fs.addFile("/c/y.txt", "hello world")
        fs.addFile("/b/z.txt", "unique content")

        finder = DuplicateFileFinder(fs)
        print(finder.findDuplicateFiles())
        # Expected: [["/a/x.txt", "/c/y.txt"]]

    @staticmethod
    def test2():
        print("===== Test 2 =====")

        fs = FileSystem()
        fs.addFile("/dir1/a.txt", "content A")
        fs.addFile("/dir2/b.txt", "content A")
        fs.addFile("/dir3/c.txt", "content A")
        largeContent = "This is a longer piece of content for testing hash computation with more data."
        fs.addFile("/docs/report.txt", largeContent)
        fs.addFile("/backup/report_copy.txt", largeContent)
        fs.addFile("/unique/file1.txt", "unique 1")
        fs.addFile("/unique/file2.txt", "unique 2")

        finder = DuplicateFileFinder(fs)
        print(finder.findDuplicateFiles())
        # Expected: [["/backup/report_copy.txt", "/docs/report.txt"], ["/dir1/a.txt", "/dir2/b.txt", "/dir3/c.txt"]]

    @staticmethod
    def test3():
        print("===== Test 3 =====")
        fs = FileSystem()
        fs.addFile("/empty/a.txt", "")
        fs.addFile("/empty/b.txt", "")
        fs.addFile("/empty/c.txt", "")
        fs.addFile("/same_size/x.txt", "abc")
        fs.addFile("/same_size/y.txt", "xyz")
        fs.addFile("/solo/only.txt", "I am alone")

        finder = DuplicateFileFinder(fs)
        print(finder.findDuplicateFiles())
        # Expected: [["/empty/a.txt", "/empty/b.txt", "/empty/c.txt"]]

if __name__ == "__main__":
    Solution.main()
