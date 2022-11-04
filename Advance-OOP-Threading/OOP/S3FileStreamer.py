class S3StreamingFileReader(object):
    """
    A wrapper around boto.s3.key.Key that allows us to stream down an S3
    file, i.e., iterate line-by-line over it, so we don't have to pull down the
    entire file at once.

    This code will work with FGAC user-access when:
     * Run from Juno (Jupyter) or MLP's TCP K8s PODs
     * Run on a devapp IF you run `hologram cvs` first

    It will NOT work with FGAC when used from:
     * Monarch workers
     * Spinner Scheduler (code run outside or while creating a DAG)
    Contact #fine-grained-access-controls FGAC help is required
    """

    def __init__(self, key, delimiter="\n", encoding="utf-8"):
        self.key = key  # this is an S3Key object
        self.encoding = encoding
        self.delimiter = text_utils.ensure_binary(delimiter, self.encoding)  # what to break lines by
        self.buffer = b""  # buffer must be bytes
        self.start_search_index = 0

    def __repr__(self):
        return "S3StreamingFileReader key:%s" % self.key.name

    def __next__(self):
        return self.next()

    def next(self):
        """Return the next "line" of the file, ending at (and including) the
        specified delimiter.

        This wraps around the boto Key.next() method, which always returns the
        next 8192 bytes and ignores newlines.

        """
        while True:
            end_of_line = self.buffer.find(self.delimiter, self.start_search_index)

            # We've found our delimiter!
            if end_of_line != -1:
                ret = self.buffer[: end_of_line + 1]
                self.start_search_index = 0
                self.buffer = self.buffer[end_of_line + 1 :]
                return ret.decode(self.encoding)

            byte_text = next(self.key)

            # End of file? Let's go home.
            if not byte_text:
                # There's still something to return.
                if self.buffer:
                    ret = self.buffer
                    self.start_search_index = 0
                    self.buffer = b""
                    return ret.decode(self.encoding)
                # We've exhausted our buffer.
                else:
                    raise StopIteration

            # Append the bytes to our buffer and hope that the next loop finds
            # something more interesting...
            else:
                self.start_search_index = len(self.buffer)
                self.buffer += byte_text

    def __iter__(self):
        return self

    def close(self):
        # Note: calling close() on a boto Key will cause it to read
        # the entire value down from S3 if it hasn't already.
        return self.key.close()




# boto.s3.key.Key
class Key:
    # returns 8kb in middle of file
    # returns < 8kb at end of file
    def next(self) -> str:
        ...

class S3StreamingFileReader(es[str]):
    def __init__(self, key: boto.s3.key.Key, delimiter: str = "\n"):
        ...

    # returns the next line from the file. If there are no
    # more records to consume, raises StopIteration
    def __next__(self) -> str:
        ...
    def __iter__(self) -> Iterator[bytes]:
        return self

class Boto3Mock:
    # private:
    _index = -1
    # private:
    _fakeData = [
        "one\ntw",
        "o\nthre",
        "e\nfour",
        "\nfive\n",
        "six\nse",
        "ven\nei",
        "ght\nni",
        "ne\nten",
        "\neleve",
        "n\noneh",
        "undred",
        "one\non",
        "ehundre",
        "dtwo\n",
        None,
    ]
    # public:
    def next(self):
        self._index = self._index + 1
        if self._index >= len(self._fakeData):
        	return None
        return self._fakeData[self._index]
