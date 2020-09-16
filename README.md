# Demo

Some description.

## Python Hash Table Implementation

There are two implementation of hash table using:
  - separate chaining;
  - open addressing with linear probing;

The main design elements of the HashMapBase class are:
  - The bucket array is represented as a Python list (self._table) with all entries initialised to None.
  - Maintain an instance variable self._n that represents the number of distinct items that are currently stored in the hash table.
  - If the load factor of the table grows above 0.5, we double the size of the table and rehash all items into the new table.
  - Define a _hash_function utility method that relies on Python's built-in hash function to produce hash codes for keys, and a randomised Multiply-Add-Divide (MAD) formula for the compression function.

The HashMapBase class presumes the following to be abstract methods:
  - _bucket_getitem(j, k)
    This method should search bucket j for an item having key k, returning the associated value, if found, or else raising a KeyError.
  - _bucket_setitem(j, k, v)
    This method should modify bucket j so that key k becomes associated with value v. If the key already exists, the new value overwrites the existing value. Otherwise, a new item is inserted and this method is responsible for incrementing self._n.
  - _bucket_delitem(j, k)
    This method should remove the item from bucket j having key k, or raise a KeyError if no such item exists. (self._n is decremented after this method.)
  - __iter__
    This is the standard map method to iterate through all keys of the map. Our base class does not delegate this on a per-bucket basis because "buckets" in open addressing are not inherently disjoint.
