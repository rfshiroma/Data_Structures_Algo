# Maps, Hash Tables, and Skip Lists

Some description.

## Maps and Dictionaries
Dictionary: It represents an abstraction in which unique keys are mapped to associated values.

Examples and applications of maps:
  - A university's information system relies on some form of student ID as a key that is mapped to that student's associated record (such as the student's name, address, and course grades) serving as the value.
  - The domain-name system (DNS) maps a host name, such as www.wiley.com, to an Internet-Protocol (IP) address, such as 208.215.179.146.
  - A social media site typically relies on a (nonnumeric) username as a key that can be efficiently mapped to a particular user’s associated information.
  - A computer graphics system may map a color name, such as turquoise , to the triple of numbers that describes the color’s RGB (red-green-blue) representation, such as (64,224,208).
  - Python uses a dictionary to represent each namespace, mapping an identifying string, such as 'pi', to an associated object, such as 3.14159.

Maps may be implemented so that a search for a key, and its associated value, can be performed very efficiently, therefore supporting fast lookup in such applications. 

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
