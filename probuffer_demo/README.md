## [Protocol Buffer Basics](https://developers.google.com/protocol-buffers/docs/pythontutorial)


### Basics

- Define message formats in a .proto file.
- Use the protocol buffer compiler.
- Use the Python protocol buffer API to write and read messages.


### Demo problem

Create a simple "address book" app that can

- read and write people's contact details to and from a file
- Each person in the address book has a name, ID, 
  email address, and a contact phone number

### Possible approaches

1. Use Python picking.
2. encode the data items into a single string
3. Serialize the data to XML
4. Protocol buffer

### How to use Protocol buffer

1. Write a `.proto` description of the data structure to store
2. The protobuf compiler creates a class that implements automatic encoding 
and parsing of the protobuf data with an efficient binary format.
3. The generated class provides getters and setters for the fields that make 
up a protobuf and take care of the details of reading and writing the protobuf
as a unit.
4. Protobuf format supports the idea of extending the format over time in such
a way that the code can still read data encoded with the old format.