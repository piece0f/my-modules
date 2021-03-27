"""
A small module created by 16 y.o. me (GH: piece0f) to simplify some methods and functions with dictionaries.
"""


class superDict(dict):
    """Class inherited from dict, with more methods and attributes"""
    def getkey(self, value, default=None) -> list:
        """Get all keys that contains given value"""
        keys = []
        for k, v in self.items():
            if v == value:
                keys.append(k)
        return keys or default

    def append(self, key, value=None):
        """Append key with value (def. None) to dict"""
        self.update({key: value})

    def sort(self, by_keys: bool = True, reverse: bool = False, filt=None):
        """REPLACING METHOD, DANGEROUS!\n\n
        Sorting dictionary by_keys (if True) or by values (if by_keys is False).
        If reverse is True, sorting reverse.
        If filt is given, items that not fits in given function are going to be removed.\n\n
        WARNING: if sorting by values, order of keys with same values may change.
        """
        sorted_dict = superDict()
        if by_keys:
            if not filt:
                sorted_dict = sorted(self, reverse=reverse)
                self.clear()
                self.update(sorted_dict)
                return
            for key in sorted(self.keys()):
                if filt(key):
                    sorted_dict.append(key, self[key])
            self.clear()
            self.update(sorted_dict)
        else:
            for value in sorted(self.values()):
                if not filt:
                    for k in self.getkey(value):
                        sorted_dict.append(k, value)
                else:
                    if filt(value):
                        for k in self.getkey(value):
                            sorted_dict.append(k, value)
            self.clear()
            self.update(sorted_dict)

    def max(self, for_key: bool = True):
        """Returns dict with max key.
        If for_key is False, returns dict with keys of max value.
        """
        if for_key:
            max_key = max(self.keys())
            return {max_key: self[max_key]}
        else:
            max_value = max(self.values())
            return {k: max_value for k in self.getkey(max_value)}
