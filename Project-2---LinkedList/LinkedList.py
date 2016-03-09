class Linked_List:

    class _Node:

        def __init__(self, val):
            self.val = val
            self.NextNode = None
            self.PrevNode = None

    def __init__(self):
        self._Header = Linked_List._Node(None)
        self._Trailer = Linked_List._Node(None)
        self._Header.NextNode = self._Trailer
        self._Trailer.PrevNode = self._Header
        self._size = 0

    def __len__(self):
        return self._size


    def append_element(self, val):
        New_Node = Linked_List._Node(val)
        if self._size == 0:
            New_Node.NextNode = self._Trailer
            New_Node.PrevNode = self._Header
            self._Header.NextNode = New_Node
            self._Trailer.PrevNode = New_Node
        else:
            New_Node.NextNode = self._Trailer
            New_Node.PrevNode = self._Trailer.PrevNode
            self._Trailer.PrevNode.NextNode = New_Node
            self._Trailer.PrevNode = New_Node
        self._size += 1


    def insert_element_at(self, val, index):
        if index >= self._size or index < 0:
            raise IndexError
        else:
            self._size += 1
            New_Node = Linked_List._Node(val)
            current = self._Header
            while index > 0 and current.NextNode.NextNode is not None:
                current = current.NextNode
                index -= 1
            New_Node.NextNode = current.NextNode
            New_Node.PrevNode = current
            New_Node.PrevNode = current
            current.NextNode.PrevNode = New_Node
            current.NextNode = New_Node


    def remove_element_at(self, index):
        if index >= self._size or index < 0:
            raise IndexError
        current = self._Header.NextNode
        while index > 0 and current.NextNode.NextNode is not None:
            current = current.NextNode
            index -= 1
        current.PrevNode.NextNode = current.NextNode
        current.NextNode.PrevNode = current.PrevNode
        current.NextNode = None
        current.PrevNode = None
        self._size -= 1
        return current.val


    def get_element_at(self, index):
        if index >= self._size or index < 0:
            raise IndexError
        index += 1
        current = self._Header
        while index > 0 and current.NextNode.NextNode is not None:
            current = current.NextNode
            index -= 1
        return current.val


    def __str__(self):
        start = "[ "
        current = self._Header.NextNode
        if self._Header.NextNode == self._Trailer:
            return "[ ]"
        else:
            while current.NextNode is not self._Trailer:
                start = start + str(current.val) + ", "
                current = current.NextNode
            start += str(current.val) + " ]"
        return start


    def __iter__(self):
        self._iter_node = self._Header
        return self

    def __next__(self):

        if self._iter_node is self._Trailer.PrevNode:
            raise StopIteration
        to_return = self._iter_node.NextNode
        self._iter_node = to_return
        return to_return.val



if __name__ == '__main__':


    print("--PRINTING EMPTY LIST--")
    a = Linked_List()
    print(a)
    print('List has ' + str(len(a)) + ' elements')
    print()
    print("--------------------------------------------------------------")
    print("--APPENDING ELEMENT IN EMPTY LIST--")
    try:
        a.append_element("HI")
    except(IndexError):
        print("Index Error Caught for Trying to Insert out of Range")
    print(a)
    print('List has ' + str(len(a)) + ' elements')
    print()
    print("--------------------------------------------------------------")


    print("--REMOVING ELEMENT FROM LIST SIZE 1--")
    try:
        a.remove_element_at(0)
    except(IndexError):
        print("Index Error Caught for Trying to Remove out of Range")
    print(a)
    print('List has ' + str(len(a)) + ' elements')
    print()


    print("--REMOVING ELEMENT FROM EMPTY LIST - SHOULD PRODUCE ERROR--")
    try:
        a.remove_element_at(0)
    except(IndexError):
        print("Index Error Caught for Trying to Remove out of Range")
    print(a)
    print('List has ' + str(len(a)) + ' elements')
    print()
    print("--------------------------------------------------------------")


    print("--INSERTING ELEMENT IN EMPTY LIST - SHOULD PRODUCE ERROR--")
    try:
        a.insert_element_at(10,0)

    except(IndexError):
        print("Index Error Caught for Trying to Insert in an empty list")
    print(a)
    print('List has ' + str(len(a)) + ' elements')
    print()
    print("--------------------------------------------------------------")

    print("--GETTING ELEMENT IN EMPTY LIST - SHOULD PRODUCE ERROR--")
    try:
        print(a.get_element_at(0))

    except IndexError:
        print("Index Error Caught for Trying to Get out of Range")
    print(a)
    print('List has ' + str(len(a)) + ' elements')
    print()
    print("--------------------------------------------------------------")

    print("--ITERATING THROUGH AN EMPTY LIST--")
    for val in a:
        print(val)
    print()
    print("--------------------------------------------------------------")


    print("--APPENDING MULTIPLE VALUES TO LIST--")
    try:
        for i in range(0,5):
            a.append_element(i)
    except(IndexError):
        print("Index Error Caught for Trying to Insert out of Range")
    print(a)
    print('List has ' + str(len(a)) + ' elements')
    print()
    print("--------------------------------------------------------------")

    print("--INSERTING ELEMENTS IN VALID INDEX--")
    try:
        a.insert_element_at(1.5,2)
        a.insert_element_at(3.5,5)

    except IndexError:
        print("Index Error Caught for Trying to Insert out of Range")
    print(a)
    print('List has ' + str(len(a)) + ' elements')
    print()

    print("--INSERTING ELEMENT IN INVALID INDEX - SHOULD PRODUCE ERROR--")
    try:
        a.insert_element_at(5,7)

    except IndexError:
        print("Index Error Caught for Trying to Insert out of Range")
    print(a)
    print('List has ' + str(len(a)) + ' elements')
    print()

    print("--INSERTING ELEMENT IN INVALID INDEX - SHOULD PRODUCE ERROR--")
    try:
        a.insert_element_at(5,-1)

    except IndexError:
        print("Index Error Caught for Trying to Insert out of Range")
    print(a)
    print('List has ' + str(len(a)) + ' elements')
    print()
    print("--------------------------------------------------------------")

    print("--REMOVING ELEMENT IN VALID INDEX--")
    try:
        print(a.remove_element_at(6))

    except IndexError:
        print("Index Error Caught for Trying to Remove out of Range")
    print(a)
    print('List has ' + str(len(a)) + ' elements')
    print()

    print("--REMOVING ELEMENT IN INVALID INDEX - SHOULD PRODUCE ERROR--")
    try:
        a.remove_element_at(6)

    except IndexError:
        print("Index Error Caught for Trying to Remove out of Range")
    print(a)
    print('List has ' + str(len(a)) + ' elements')
    print()

    print("--REMOVING ELEMENT IN INVALID INDEX - SHOULD PRODUCE ERROR--")
    try:
        a.remove_element_at(-1)

    except IndexError:
        print("Index Error Caught for Trying to Remove out of Range")
    print(a)
    print('List has ' + str(len(a)) + ' elements')
    print()
    print("--------------------------------------------------------------")

    print("--GETTING ELEMENT IN VALID INDEX--")
    try:
        print(a.get_element_at(3))

    except IndexError:
        print("Index Error Caught for Trying to Get out of Range")
    print(a)
    print('List has ' + str(len(a)) + ' elements')
    print()

    print("--GETTING ELEMENT IN INVALID INDEX - SHOULD PRODUCE ERROR--")
    try:
        print(a.get_element_at(a._size))

    except IndexError:
        print("Index Error Caught for Trying to Get out of Range")
    print(a)
    print('List has ' + str(len(a)) + ' elements')
    print()

    print("--GETTING ELEMENT IN INVALID INDEX - SHOULD PRODUCE ERROR--")
    try:
        a.get_element_at(-1)

    except IndexError:
        print("Index Error Caught for Trying to Get out of Range")
    print(a)
    print('List has ' + str(len(a)) + ' elements')
    print()
    print("--------------------------------------------------------------")


    print()
    print(a)
    print("TESTING ITERATOR")
    for val in a:
        print(val)

    print("--------------------------------------------------------------")
    print("--APPENDING ELEMENT IN VALID INDEX--")
    try:
        a.append_element(10)
        a.append_element(10)

    except IndexError:
        print("Index Error Caught for Trying to Get out of Range")

    print(a)
    print('List has ' + str(len(a)) + ' elements')
    print()
    print("--------------------------------------------------------------")
    print("--REMOVING ELEMENT IN INVALID INDEX - SHOULD PRODUCE ERROR--")
    try:
        a.remove_element_at(8)

    except IndexError:
        print("Index Error Caught for Trying to Remove out of Range")

    print(a)
    print('List has ' + str(len(a)) + ' elements')
    print()
    print("--------------------------------------------------------------")
    print("--INSERTING ELEMENT IN INVALID INDEX - SHOULD PRODUCE ERROR--")
    try:
        a.insert_element_at(5,8)

    except IndexError:
        print("Index Error Caught for Trying to Insert out of Range")
    print(a)
    print('List has ' + str(len(a)) + ' elements')
    print()

    print("--------------------------------------------------------------")
    print(a)
    print(len(a))


    print("--------------------------------------------------------------")
    print("--REMOVING ELEMENT FROM VALID INDEX--")
    try:
        for i in range(7, 0, -1):
            a.remove_element_at(i)
    except(IndexError):
        print("Index Error Caught for Trying to Remove out of Range")
    print(a)
    print('List has ' + str(len(a)) + ' elements')
    print()

    print("--------------------------------------------------------------")
    print("--INSERTING ELEMENT IN VALID INDEX--")
    try:
        a.insert_element_at(10,0)

    except(IndexError):
        print("Index Error Caught for Trying to Insert in an empty list")
    print(a)
    print('List has ' + str(len(a)) + ' elements')
    print()

    print("***10 removed")
    a.remove_element_at(0)

    print("--INSERTING ELEMENT IN INVALID INDEX - SHOULD PRODUCE ERROR--")
    try:
        a.insert_element_at(5,1)

    except IndexError:
        print("Index Error Caught for Trying to Insert out of Range")
    print(a)
    print('List has ' + str(len(a)) + ' elements')
    print()
    print("--------------------------------------------------------------")
    print("--GETTING ELEMENT IN VALID INDEX--")
    try:
        print(a.get_element_at(0))

    except IndexError:
        print("Index Error Caught for Trying to Get out of Range")
    print(a)
    print('List has ' + str(len(a)) + ' elements')
    print()

    print("--GETTING ELEMENT IN INVALID INDEX - SHOULD PRODUCE ERROR--")
    try:
        print(a.get_element_at(1))

    except IndexError:
        print("Index Error Caught for Trying to Get out of Range")
    print(a)
    print('List has ' + str(len(a)) + ' elements')
    print()
    print("--------------------------------------------------------------")
    for val in a:
        print(val)


