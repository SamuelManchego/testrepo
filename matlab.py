{
  "metadata": {
    "kernelspec": {
      "name": "python",
      "display_name": "Pyolite",
      "language": "python"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "python",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8"
    }
  },
  "nbformat_minor": 4,
  "nbformat": 4,
  "cells": [
    {
      "cell_type": "markdown",
      "source": "<p style=\"text-align:center\">\n    <a href=\"https://skills.network/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2022-01-01\">\n    <img src=\"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png\" width=\"200\" alt=\"Skills Network Logo\"  />\n    </a>\n</p>\n\n# String Operations\n\nEstimated time needed: **15** minutes\n\n## Objectives\n\nAfter completing this lab you will be able to:\n\n*   Work with Strings\n*   Perform operations on String\n*   Manipulate Strings using indexing and escape sequences\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "<h2>Table of Contents</h2>\n<div class=\"alert alert-block alert-info\" style=\"margin-top: 20px\">\n    <ul>\n        <li>\n            <a href=\"https://#strings\">What are Strings?</a>\n        </li>\n        <li>\n            <a href=\"https://#index\">Indexing</a>\n            <ul>\n                <li><a href=\"https://neg/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2022-01-01\">Negative Indexing</a></li>\n                <li><a href=\"https://slice/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2022-01-01\">Slicing</a></li>\n                <li><a href=\"https://stride/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2022-01-01\">Stride</a></li>\n                <li><a href=\"https://concat/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2022-01-01\">Concatenate Strings</a></li>\n            </ul>\n        </li>\n        <li>\n            <a href=\"https://#escape\">Escape Sequences</a>\n        </li>\n        <li>\n            <a href=\"https://#operations\">String Operations</a>\n        </li>\n        <li>\n            <a href=\"https://#quiz\">Quiz on Strings</a>\n        </li>\n    </ul>\n\n</div>\n\n<hr>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "<h2 id=\"strings\">What are Strings?</h2>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "The following example shows a string contained within 2 quotation marks:\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# Use quotation marks for defining string\n\n\"Michael Jackson\"",
      "metadata": {
        "trusted": true
      },
      "execution_count": 1,
      "outputs": [
        {
          "execution_count": 1,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'Michael Jackson'"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "We can also use single quotation marks:\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# Use single quotation marks for defining string\n\n'Michael Jackson'",
      "metadata": {
        "trusted": true
      },
      "execution_count": 2,
      "outputs": [
        {
          "execution_count": 2,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'Michael Jackson'"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "A string can be a combination of spaces and digits:\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# Digitals and spaces in string\n\n'1 2 3 4 5 6 '",
      "metadata": {
        "trusted": true
      },
      "execution_count": 3,
      "outputs": [
        {
          "execution_count": 3,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'1 2 3 4 5 6 '"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "A string can also be a combination of special characters :\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# Special characters in string\n\n'@#2_#]&*^%$'",
      "metadata": {
        "trusted": true
      },
      "execution_count": 4,
      "outputs": [
        {
          "execution_count": 4,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'@#2_#]&*^%$'"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "We can print our string using the print statement:\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# Print the string\n\nprint(\"hello!\")",
      "metadata": {
        "trusted": true
      },
      "execution_count": 5,
      "outputs": [
        {
          "name": "stdout",
          "text": "hello!\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "We can bind or assign a string to another variable:\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# Assign string to variable\n\nname = \"Michael Jackson\"\nname",
      "metadata": {
        "trusted": true
      },
      "execution_count": 6,
      "outputs": [
        {
          "execution_count": 6,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'Michael Jackson'"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "<hr>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "<h2 id=\"index\">Indexing</h2>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "It is helpful to think of a string as an ordered sequence. Each element in the sequence can be accessed using an index represented by the array of numbers:\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "<img src=\"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%201/images/StringsIndex.png\" width=\"600\" align=\"center\">\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "The first index can be accessed as follows:\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "<hr/>\n<div class=\"alert alert-success alertsuccess\" style=\"margin-top: 20px\">\n[Tip]: Because indexing starts at 0, it means the first index is on the index 0.\n</div>\n<hr/>\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# Print the first element in the string\n\nprint(name[0])",
      "metadata": {
        "trusted": true
      },
      "execution_count": 7,
      "outputs": [
        {
          "name": "stdout",
          "text": "M\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "We can access index 6:\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# Print the element on index 6 in the string\n\nprint(name[6])",
      "metadata": {
        "trusted": true
      },
      "execution_count": 8,
      "outputs": [
        {
          "name": "stdout",
          "text": "l\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "Moreover, we can access the 13th index:\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# Print the element on the 13th index in the string\n\nprint(name[13])",
      "metadata": {
        "trusted": true
      },
      "execution_count": 9,
      "outputs": [
        {
          "name": "stdout",
          "text": "o\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "<h3 id=\"neg\">Negative Indexing</h3>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "We can also use negative indexing with strings:\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "<img src=\"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%201/images/StringsNeg.png\" width=\"600\" align=\"center\">\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "Negative index can help us to count the element from the end of the string.\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "The last element is given by the index -1:\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# Print the last element in the string\n\nprint(name[-1])",
      "metadata": {
        "trusted": true
      },
      "execution_count": 10,
      "outputs": [
        {
          "name": "stdout",
          "text": "n\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "The first element can be obtained by  index -15:\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# Print the first element in the string\n\nprint(name[-15])",
      "metadata": {
        "trusted": true
      },
      "execution_count": 11,
      "outputs": [
        {
          "name": "stdout",
          "text": "M\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "We can find the number of characters in a string by using <code>len</code>, short for length:\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# Find the length of string\n\nlen(\"Michael Jackson\")",
      "metadata": {
        "trusted": true
      },
      "execution_count": 12,
      "outputs": [
        {
          "execution_count": 12,
          "output_type": "execute_result",
          "data": {
            "text/plain": "15"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "<h3 id=\"slice\">Slicing</h3>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "We can obtain multiple characters from a string using slicing, we can obtain the 0 to 4th and 8th to the 12th element:\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "<img src=\"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%201/images/StringsSlice.png\" width=\"600\" align=\"center\">\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "<hr/>\n<div class=\"alert alert-success alertsuccess\" style=\"margin-top: 20px\">\n[Tip]: When taking the slice, the first number means the index (start at 0), and the second number means the length from the index to the last element you want (start at 1)\n</div>\n<hr/>\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# Take the slice on variable name with only index 0 to index 3\n\nname[0:4]",
      "metadata": {
        "trusted": true
      },
      "execution_count": 13,
      "outputs": [
        {
          "execution_count": 13,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'Mich'"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": "# Take the slice on variable name with only index 8 to index 11\n\nname[8:12]",
      "metadata": {
        "trusted": true
      },
      "execution_count": 14,
      "outputs": [
        {
          "execution_count": 14,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'Jack'"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "<h3 id=\"stride\">Stride</h3>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "We can also  input a stride value as follows, with the '2' indicating that we are selecting every second variable:\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "<img src=\"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%201/images/StringsStride.png\" width=\"600\" align=\"center\">\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# Get every second element. The elments on index 1, 3, 5 ...\n\nname[::2]",
      "metadata": {
        "trusted": true
      },
      "execution_count": 15,
      "outputs": [
        {
          "execution_count": 15,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'McalJcsn'"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "We can also incorporate slicing  with the stride. In this case, we select the first five elements and then use the stride:\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# Get every second element in the range from index 0 to index 4\n\nname[0:5:2]",
      "metadata": {
        "trusted": true
      },
      "execution_count": 16,
      "outputs": [
        {
          "execution_count": 16,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'Mca'"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "<h3 id=\"concat\">Concatenate Strings</h3>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "We can concatenate or combine strings by using the addition symbols, and the result is a new string that is a combination of both:\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# Concatenate two strings\n\nstatement = name + \" is the best\"\nstatement",
      "metadata": {
        "trusted": true
      },
      "execution_count": 19,
      "outputs": [
        {
          "execution_count": 19,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'Michael Jackson is the best'"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "To replicate values of a string we simply multiply the string by the number of times we would like to replicate it. In this case, the number is three. The result is a new string, and this new string consists of three copies of the original string:\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# Print the string for 3 times\n\n3 * \"Michael Jackson\"",
      "metadata": {
        "trusted": true
      },
      "execution_count": 20,
      "outputs": [
        {
          "execution_count": 20,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'Michael JacksonMichael JacksonMichael Jackson'"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "You can create a new string by setting it to the original variable. Concatenated  with a new string, the result is a new string that changes from Michael Jackson to “Michael Jackson is the best\".\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# Concatenate strings\n\nname = \"Michael Jackson\"\nname = name + \" is the best\"\nname",
      "metadata": {
        "trusted": true
      },
      "execution_count": 21,
      "outputs": [
        {
          "execution_count": 21,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'Michael Jackson is the best'"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "<hr>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "<h2 id=\"escape\">Escape Sequences</h2>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "Back slashes represent the beginning  of escape sequences. Escape sequences represent strings that may be difficult to input. For example, back slash \"n\" represents a new line. The output is given by a new line after the back slash \"n\" is encountered:\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# New line escape sequence\n\nprint(\" Michael Jackson \\n is the best\" )",
      "metadata": {
        "trusted": true
      },
      "execution_count": 22,
      "outputs": [
        {
          "name": "stdout",
          "text": " Michael Jackson \n is the best\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "Similarly, back slash  \"t\" represents a tab:\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# Tab escape sequence\n\nprint(\" Michael Jackson \\t is the best\" )",
      "metadata": {
        "trusted": true
      },
      "execution_count": 23,
      "outputs": [
        {
          "name": "stdout",
          "text": " Michael Jackson \t is the best\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "If you want to place a back slash in your string, use a double back slash:\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# Include back slash in string\n\nprint(\" Michael Jackson \\\\ is the best\" )",
      "metadata": {
        "trusted": true
      },
      "execution_count": 24,
      "outputs": [
        {
          "name": "stdout",
          "text": " Michael Jackson \\ is the best\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "We can also place an \"r\" before the string to display the backslash:\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# r will tell python that string will be display as raw string\n\nprint(r\" Michael Jackson \\ is the best\" )",
      "metadata": {
        "trusted": true
      },
      "execution_count": 25,
      "outputs": [
        {
          "name": "stdout",
          "text": " Michael Jackson \\ is the best\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "<hr>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "<h2 id=\"operations\">String Operations</h2>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "There are many string operation methods in Python that can be used to manipulate the data. We are going to use some basic string operations on the data.\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "Let's try with the method <code>upper</code>; this method converts lower case characters to upper case characters:\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# Convert all the characters in string to upper case\n\na = \"Thriller is the sixth studio album\"\nprint(\"before upper:\", a)\nb = a.upper()\nprint(\"After upper:\", b)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 27,
      "outputs": [
        {
          "name": "stdout",
          "text": "before upper: Thriller is the sixth studio album\nAfter upper: THRILLER IS THE SIXTH STUDIO ALBUM\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "Let's try with the method <code>lower</code>; this method converts upper case characters to lower case characters:\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# Convert all the characters in string to lower case\na = \"MICHAEL JACKSON IS THE BEST\"\nprint(\"Before lower:\", a)\nb = a.lower()\nprint(\"After lower:\", b)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 28,
      "outputs": [
        {
          "name": "stdout",
          "text": "Before lower: MICHAEL JACKSON IS THE BEST\nAfter lower: michael jackson is the best\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "The method <code>replace</code> replaces a segment of the string, i.e. a substring  with a new string. We input the part of the string we would like to change. The second argument is what we would like to exchange the segment with, and the result is a new string with the segment changed:\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "a = \"Michael Jackson is the best\"\nb = a.replace('Michael', 'Janet')\nb",
      "metadata": {
        "trusted": true
      },
      "execution_count": 29,
      "outputs": [
        {
          "execution_count": 29,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'Janet Jackson is the best'"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": "# Replace the old substring with the new target substring by removing some punctuations.\n\na = \"Hello! Michael Jackson has: 12 characters.\"\nprint(a)\nb = a.replace('!','').replace(':','').replace('.','')\nprint(b)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 30,
      "outputs": [
        {
          "name": "stdout",
          "text": "Hello! Michael Jackson has: 12 characters.\nHello Michael Jackson has 12 characters\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "The method <code>find</code> finds a sub-string. The argument is the substring you would like to find, and the output is the first index of the sequence. We can find the sub-string <code>jack</code> or <code>el<code>.\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "<img src=\"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%201/images/StringsFind.png\" width=\"600\" align=\"center\">\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# Find the substring in the string. Only the index of the first elment of substring in string will be the output\n\nname = \"Michael Jackson\"\nname.find('el')",
      "metadata": {
        "trusted": true
      },
      "execution_count": 31,
      "outputs": [
        {
          "execution_count": 31,
          "output_type": "execute_result",
          "data": {
            "text/plain": "5"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": "# Find the substring in the string.\n\nname.find('Jack')",
      "metadata": {
        "trusted": true
      },
      "execution_count": 32,
      "outputs": [
        {
          "execution_count": 32,
          "output_type": "execute_result",
          "data": {
            "text/plain": "8"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "If the  sub-string is not in the string then the output is a negative one. For example, the string 'Jasdfasdasdf' is not a substring:\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# If cannot find the substring in the string\n\nname.find('Jasdfasdasdf')",
      "metadata": {
        "trusted": true
      },
      "execution_count": 33,
      "outputs": [
        {
          "execution_count": 33,
          "output_type": "execute_result",
          "data": {
            "text/plain": "-1"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "The method <code>Split</code> splits the string at the specified separator, and returns a list:\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#Split the substring into list\nname = \"Michael Jackson\"\nsplit_string = (name.split())\nsplit_string",
      "metadata": {
        "trusted": true
      },
      "execution_count": 34,
      "outputs": [
        {
          "execution_count": 34,
          "output_type": "execute_result",
          "data": {
            "text/plain": "['Michael', 'Jackson']"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "## RegEx\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "In Python, RegEx (short for Regular Expression) is a tool for matching and handling strings. \n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "This RegEx module provides several functions for working with regular expressions, including <code>search, split, findall,</code> and <code>sub</code>. \n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "Python provides a built-in module called <code>re</code>, which allows you to work with regular expressions. \nFirst, import the <code>re</code> module\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "import re",
      "metadata": {
        "trusted": true
      },
      "execution_count": 35,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": "The search() function searches for specified patterns within a string. Here is an example that explains how to use the search() function to search for the word \"Jackson\" in the string \"Michael Jackson is the best\".\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "s1 = \"Michael Jackson is the best\"\n\n# Define the pattern to search for\npattern = r\"Jackson\"\n\n# Use the search() function to search for the pattern in the string\nresult = re.search(pattern, s1)\n\n# Check if a match was found\nif result:\n    print(\"Match found!\")\nelse:\n    print(\"Match not found.\")\n",
      "metadata": {
        "trusted": true
      },
      "execution_count": 38,
      "outputs": [
        {
          "name": "stdout",
          "text": "Match found!\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "Regular expressions (RegEx) are patterns used to match and manipulate strings of text. There are several special sequences in RegEx that can be used to match specific characters or patterns.\n\n| Special Sequence | Meaning                 | \tExample             |\n| -----------  | ----------------------- | ----------------------|\n| \\d|Matches any digit character (0-9)|\"123\" matches \"\\d\\d\\d\"|\n|\\D|Matches any non-digit character|\"hello\" matches \"\\D\\D\\D\\D\\D\"|\n|\\w|Matches any word character (a-z, A-Z, 0-9, and _)|\"hello_world\" matches \"\\w\\w\\w\\w\\w\\w\\w\\w\\w\"|\n|\\W|Matches any non-word character|\t\"@#$%\" matches \"\\W\\W\\W\\W\"|\n|\\s|Matches any whitespace character (space, tab, newline, etc.)|\"hello world\" matches \"\\w\\s\\w\\w\\w\\w\\w\"|\n|\\S|Matches any non-whitespace character|\"hello_world\" matches \"\\S\\S\\S\\S\\S\\S\\S\\S\\S\"|\n|\\b|Matches the boundary between a word character and a non-word character|\"cat\" matches \"\\bcat\\b\" in \"The cat sat on the mat\"|\n|\\B|Matches any position that is not a word boundary|\"cat\" matches \"\\Bcat\\B\" in \"category\" but not in \"The cat sat on the mat\"|\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "Special Sequence Examples:\n\nA simple example of using the <code>\\d</code> special sequence in a regular expression pattern with Python code:\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "pattern = r\"\\d\\d\\d\\d\\d\\d\\d\\d\\d\\d\"  # Matches any ten consecutive digits\ntext = \"My Phone number is 1234567890\"\nmatch = re.search(pattern, text)\n\nif match:\n    print(\"Phone number found:\", match.group())\nelse:\n    print(\"No match\")",
      "metadata": {
        "trusted": true
      },
      "execution_count": 39,
      "outputs": [
        {
          "name": "stdout",
          "text": "Phone number found: 1234567890\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "The regular expression pattern is defined as r\"\\d\\d\\d\\d\\d\\d\\d\\d\\d\\d\", which uses the \\d special sequence to match any digit character (0-9), and the \\d sequence is repeated ten times to match ten consecutive digits\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "A simple example of using the <code>\\W</code> special sequence in a regular expression pattern with Python code:\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "pattern = r\"\\W\"  # Matches any non-word character\ntext = \"Hello, world!\"\nmatches = re.findall(pattern, text)\n\nprint(\"Matches:\", matches)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 42,
      "outputs": [
        {
          "name": "stdout",
          "text": "Matches: [',', ' ', '!']\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "The regular expression pattern is defined as r\"\\W\", which uses the \\W special sequence to match any character that is not a word character (a-z, A-Z, 0-9, or _). The string we're searching for matches in is \"Hello, world!\".\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "The <code>findall()</code> function finds all occurrences of a specified pattern within a string.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "s2 = \"Michael Jackson was a singer and known as the 'King of Pop'\"\n\n\n# Use the findall() function to find all occurrences of the \"as\" in the string\nresult = re.findall(\"as\", s2)\n\n# Print out the list of matched words\nprint(result)\n",
      "metadata": {
        "trusted": true
      },
      "execution_count": 45,
      "outputs": [
        {
          "name": "stdout",
          "text": "['as', 'as']\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "A regular expression's <code>split()</code> function splits a string into an array of substrings based on a specified pattern.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# Use the split function to split the string by the \"\\s\"\nsplit_array = re.split(\"\\s\", s2)\n\n# The split_array contains all the substrings, split by whitespace characters\nprint(split_array) ",
      "metadata": {
        "trusted": true
      },
      "execution_count": 46,
      "outputs": [
        {
          "name": "stdout",
          "text": "['Michael', 'Jackson', 'was', 'a', 'singer', 'and', 'known', 'as', 'the', \"'King\", 'of', \"Pop'\"]\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "The <code>sub</code> function of a regular expression in Python is used to replace all occurrences of a pattern in a string with a specified replacement.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# Define the regular expression pattern to search for\npattern = r\"King of Pop\"\n\n# Define the replacement string\nreplacement = \"legend\"\n\n# Use the sub function to replace the pattern with the replacement string\nnew_string = re.sub(pattern, replacement, s2, flags=re.IGNORECASE)\n\n# The new_string contains the original string with the pattern replaced by the replacement string\nprint(new_string) ",
      "metadata": {
        "trusted": true
      },
      "execution_count": 47,
      "outputs": [
        {
          "name": "stdout",
          "text": "Michael Jackson was a singer and known as the 'legend'\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "<hr>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "<h2 id=\"quiz\">Quiz on Strings</h2>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "What is the value of the variable <code>a</code> after the following code is executed?\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# Write your code below and press Shift+Enter to execute \n\na = \"1\"\na",
      "metadata": {
        "trusted": true
      },
      "execution_count": 52,
      "outputs": [
        {
          "execution_count": 52,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'1'"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "<details><summary>Click here for the solution</summary>\n\n```python\n\"1\"\n\n```\n\n</details>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "What is the value of the variable <code>b</code> after the following code is executed?\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# Write your code below and press Shift+Enter to execute\n\nb = \"2\"\nb",
      "metadata": {
        "trusted": true
      },
      "execution_count": 53,
      "outputs": [
        {
          "execution_count": 53,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'2'"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "<details><summary>Click here for the solution</summary>\n\n```python\n\"2\"\n\n```\n\n</details>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "What is the value of the variable <code>c</code> after the following code is executed?\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# Write your code below and press Shift+Enter to execute \n\nc = a + b\na+b",
      "metadata": {
        "trusted": true
      },
      "execution_count": 54,
      "outputs": [
        {
          "execution_count": 54,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'12'"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "<details><summary>Click here for the solution</summary>\n\n```python\n\"12\"\n\n```\n\n</details>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "<hr>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "Consider the variable <code>d</code> use slicing to print out the first three elements:\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# Write your code below and press Shift+Enter to execute\n\nd = \"ABCDEFG\"\nprint(d[:3])",
      "metadata": {
        "trusted": true
      },
      "execution_count": 55,
      "outputs": [
        {
          "name": "stdout",
          "text": "ABC\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "<details><summary>Click here for the solution</summary>\n\n```python\nprint(d[:3]) \n\n# or \n\nprint(d[0:3])\n\n```\n\n</details>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "<hr>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "Use a stride value of 2 to print out every second character of the string <code>e</code>:\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# Write your code below and press Shift+Enter to execute\n\ne = 'clocrkr1e1c1t'\nprint(e[::2])",
      "metadata": {
        "trusted": true
      },
      "execution_count": 57,
      "outputs": [
        {
          "name": "stdout",
          "text": "correct\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "<details><summary>Click here for the solution</summary>\n\n```python\nprint(e[::2])\n\n```\n\n</details>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "<hr>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "Print out a backslash:\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# Write your code below and press Shift+Enter to execute\nprint(r\"\\ \")\nprint(\"\\\\\\\\\\\\\")",
      "metadata": {
        "trusted": true
      },
      "execution_count": 61,
      "outputs": [
        {
          "name": "stdout",
          "text": "\\ \n\\\\\\\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "<details><summary>Click here for the solution</summary>\n\n```python\nprint(\"\\\\\\\\\\\\\")\n\nor\n\nprint(r\"\\ \")\n\n```\n\n</details>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "<hr>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "Convert the variable <code>f</code> to uppercase:\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# Write your code below and press Shift+Enter to execute\n\nf = \"You are wrong\"\nf.upper()",
      "metadata": {
        "trusted": true
      },
      "execution_count": 63,
      "outputs": [
        {
          "execution_count": 63,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'YOU ARE WRONG'"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "<details><summary>Click here for the solution</summary>\n\n```python\nf.upper()\n\n```\n\n</details>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "Convert the variable <code>f2</code> to lowercase:\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# Write your code below and press Shift+Enter to execute\nf2=\"YOU ARE RIGHT\"\nf2.lower()",
      "metadata": {
        "trusted": true
      },
      "execution_count": 64,
      "outputs": [
        {
          "execution_count": 64,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'you are right'"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "<details><summary>Click here for the solution</summary>\n\n```python\nf2.lower()\n\n```\n\n</details>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "<hr>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "Consider the variable <code>g</code>, and find the first index of the sub-string <code>snow</code>:\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# Write your code below and press Shift+Enter to execute\n\ng = \"Mary had a little lamb Little lamb, little lamb Mary had a little lamb \\\nIts fleece was white as snow And everywhere that Mary went Mary went, Mary went \\\nEverywhere that Mary went The lamb was sure to go\"\ng.find(\"snow\")",
      "metadata": {
        "trusted": true
      },
      "execution_count": 65,
      "outputs": [
        {
          "execution_count": 65,
          "output_type": "execute_result",
          "data": {
            "text/plain": "95"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "<details><summary>Click here for the solution</summary>\n\n```python\ng.find(\"snow\")\n\n```\n\n</details>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "In the variable <code>g</code>, replace the sub-string <code>Mary</code> with <code>Bob</code>:\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# Write your code below and press Shift+Enter to execute\ng.replace(\"Mary\", \"Bob\")",
      "metadata": {
        "trusted": true
      },
      "execution_count": 67,
      "outputs": [
        {
          "execution_count": 67,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'Bob had a little lamb Little lamb, little lamb Bob had a little lamb Its fleece was white as snow And everywhere that Bob went Bob went, Bob went Everywhere that Bob went The lamb was sure to go'"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "<details><summary>Click here for the solution</summary>\n\n```python\ng.replace(\"Mary\", \"Bob\")\n\n```\n\n</details>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "In the variable <code>g</code>, replace the sub-string <code>,</code> with <code>.</code>:\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# Write your code below and press Shift+Enter to execute\ng.replace(',', '.')",
      "metadata": {
        "trusted": true
      },
      "execution_count": 70,
      "outputs": [
        {
          "execution_count": 70,
          "output_type": "execute_result",
          "data": {
            "text/plain": "'Mary had a little lamb Little lamb. little lamb Mary had a little lamb Its fleece was white as snow And everywhere that Mary went Mary went. Mary went Everywhere that Mary went The lamb was sure to go'"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "<details><summary>Click here for the solution</summary>\n\n```python\ng.replace(',','.')\n\n```\n\n</details>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "In the variable <code>g</code>, split the substring to list:\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# Write your code below and press Shift+Enter to execute\ng.split()",
      "metadata": {
        "trusted": true
      },
      "execution_count": 71,
      "outputs": [
        {
          "execution_count": 71,
          "output_type": "execute_result",
          "data": {
            "text/plain": "['Mary',\n 'had',\n 'a',\n 'little',\n 'lamb',\n 'Little',\n 'lamb,',\n 'little',\n 'lamb',\n 'Mary',\n 'had',\n 'a',\n 'little',\n 'lamb',\n 'Its',\n 'fleece',\n 'was',\n 'white',\n 'as',\n 'snow',\n 'And',\n 'everywhere',\n 'that',\n 'Mary',\n 'went',\n 'Mary',\n 'went,',\n 'Mary',\n 'went',\n 'Everywhere',\n 'that',\n 'Mary',\n 'went',\n 'The',\n 'lamb',\n 'was',\n 'sure',\n 'to',\n 'go']"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "<details><summary>Click here for the solution</summary>\n\n```python\ng.split()\n\n```\n\n</details>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "In the string <code>s3</code>, find the four consicutive digit character using <code>\\d</code> and <code>search() </code>function:\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "s3 = \"House number- 1105\"\n\n# Write your code below and press Shift+Enter to execute\n\nresult = re.search(\"\\d\", s3)\nif result:\n    print(\"Digit found\")\n    \nelse:\n    print(\"Digit not found\")",
      "metadata": {
        "trusted": true
      },
      "execution_count": 76,
      "outputs": [
        {
          "name": "stdout",
          "text": "Digit found\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "<details><summary>Click here for the solution</summary>\n\n```python\n# Use the search() function to search for the \"\\d\" in the string\nresult = re.search(\"\\d\", s3)\n\n# Check if a match was found\nif result:\n    print(\"Digit found\")\nelse:\n    print(\"Digit not found.\")\n```\n\n</details>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "In the string <code>str1</code>, replace the sub-string <code>fox</code> with <code>bear</code> using <code>sub() </code>function:\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "str1= \"The quick brown fox jumps over the lazy dog.\"\n\n# Write your code below and press Shift+Enter to execute\nnew_str1 = re.sub(r\"fox\", \"bear\", str1)\nprint(new_str1)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 78,
      "outputs": [
        {
          "name": "stdout",
          "text": "The quick brown bear jumps over the lazy dog.\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "<details><summary>Click here for the solution</summary>\n\n```python\n# Use re.sub() to replace \"fox\" with \"bear\"\nnew_str1 = re.sub(r\"fox\", \"bear\", str1)\n\nprint(new_str1)\n```\n\n</details>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "In the string <code>str2</code> find all the occurrences of <code>woo</code> using <code>findall()</code> function:\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "str2= \"How much wood would a woodchuck chuck, if a woodchuck could chuck wood?\"\n\n# Write your code below and press Shift+Enter to execute\nmatches = re.findall(r\"woo\", str2)\nprint(matches)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 80,
      "outputs": [
        {
          "name": "stdout",
          "text": "['woo', 'woo', 'woo', 'woo']\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "<details><summary>Click here for the solution</summary>\n\n```python\n# Use re.findall() to find all occurrences of \"woo\"\nmatches = re.findall(r\"woo\", str2)\n\nprint(matches)\n```\n\n</details>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "<hr>\n<h2>The last exercise!</h2>\n<p>Congratulations, you have completed your first lesson and hands-on lab in Python.\n<hr>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "## Author\n\n<a href=\"https://www.linkedin.com/in/joseph-s-50398b136/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2022-01-01\">Joseph Santarcangelo</a>\n\n## Change Log\n\n| Date (YYYY-MM-DD) | Version | Changed By | Change Description                  |\n| ----------------- | ------- | ---------- | ----------------------------------- |\n| 2022-12-28        | 2.2     | Pratiksha  | Updated exercises                    |\n| 2022-01-10        | 2.1     | Malika     | Removed the readme for GitShare     |\n| 2020-11-11        | 2.1     | Aije       | Updated variable names to lowercase |\n| 2020-08-26        | 2.0     | Lavanya    | Moved lab to course repo in GitLab  |\n\n## <h3 align=\"center\"> © IBM Corporation 2020. All rights reserved. <h3/>\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "",
      "metadata": {},
      "execution_count": null,
      "outputs": []
    }
  ]
}
