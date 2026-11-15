    def my_print(self):
        """Prints the square with the character #.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
            return
        for _ in range(self.__size):
            print("#" * self.__size)
