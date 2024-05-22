#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

/**
 * Cesar encryption and decryption program
 * @author Pierre Maurice Schwang
 * @copyright 2020 Pierre Maurice Schwang
 */

/**
 * Defines the charset of characters which should be encoded.
 * The cesar encryption is typically case insensitive, so we only use the alphabet in lowercase.
 */
#define CHARSET "abcdefghijklmnopqrstuvwxyz"

/**
 * Encrypts a passed input based on the cesar algorithm.
 * If invalid data was passed, the program will exit and notify the user about the problem.
 * @param input The string to encrypt.
 * @return The encrypted cesar string.
 */
char *cesar_encrypt(char *input, unsigned int shift);

/**
 * Decrypts a passed input based on the cesar algorithm.
 * If invalid data was passed, the program will exit and notify the user about the problem.
 * @param input The string to decrypt.
 * @return The decrypted readable string.
 */
char *cesar_decrypt(char *input, int shift);

/**
 * Utility method to lowercase a complete char array.
 * Required for cesar_encrypt, because the cesar encryption is case insensitive.
 * @param input The string to lowercase.
 * @return The lowercase string.
 */
char *lowercase(char *input);

/**
 * Prompts the user to define the shift amount for the encryption & decryption.
 * (shift = how many times the characters should be moved to the right).
 * @return The inputted shift.
 */
int parse_shift_input();

/**
 * Reads the content of the passed file.
 * 
 * @param fileName The path to the file.
 * @return The file content or NULL if an error occourred.
 */
char *read_file(char *fileName);

/**
 * Writes data to a file.
 * 
 * @param fileName The path to the file.
 */
void write_file(char *fileName, char *content);

/**
 * Program initialization
 * @return the exit code
 */
int main()
{
	// Parse the provided shift by the user and validate.
	int shift = parse_shift_input();
	if (shift < 0)
	{
		printf("Incorrect shift input - Exiting program!");
		return 1;
	}

	// Print all available options the user can select from.
	printf("##############################################\n");
	printf("#        Cesar Encryption /Decryption        #\n");
	printf("##############################################\n");
	printf("#                                            #\n");
	printf("#   1. Encrypt input                         #\n");
	printf("#   2. Decrypt input                         #\n");
	printf("#   3. Encrypt file                          #\n");
	printf("#   4. Decrypt file                          #\n");
	printf("#                                            #\n");
	printf("#   5. Exit                                  #\n");
	printf("#                                            #\n");
	printf("##############################################\n\n");

	// Parse the selected option by the user
	int option;
	printf("Select your action: ");
	scanf("%d", &option);
	// Removes the trailing new line character, which fixes an issue related to fgets()
	getchar();

	// Defines the buffer (memory size) for the input which can be provided by the user.
	char input[2048];
	switch (option)
	{
	case 1: // Menu entry: "Encrypt input"
		printf("What should be encrypted? \n > ");
		// Read the input provided by the user.
		fgets(input, 2048, stdin);
		// Print the encrypted input using the cesar algorithm.
		printf("%s", cesar_encrypt(input, shift));
		break;
	case 2: // Menu entry: "Encrypt input"
		printf("What should be decrypted? \n > ");
		// Read the input provided by the user.
		fgets(input, 2048, stdin);
		// Print the decrypted input using the cesar algorithm.
		printf("%s", cesar_decrypt(input, shift));
		break;
	case 3: // Menu entry: "Encrypt file"
		printf("Enter the file name: \n > ");
		// Read the input provided by the user (The file name).
		scanf("%s", &input);
		// Validate the provided file name (existence, ...) and read its content.
		char *content = read_file(input);
		if (content == NULL)
			return 1;
		// Write the encrypted file content to a new (or existing) file with the name of the file + the suffix ".out.txt"
		write_file(strcat(input, ".out.txt"), cesar_encrypt(content, shift));
		break;
	case 4: // Menu entry: "Decrypt file"
		printf("Enter the file name: \n > ");
		// Read the input provided by the user (The file name).
		scanf("%s", &input);
		// Validate the provided file name (existence, ...) and read its content.
		content = read_file(input);
		if (content == NULL)
			return 1;
		// Write the decrypted file content to a new (or existing) file with the name of the file + the suffix ".out.txt"
		write_file(strcat(input, ".out.txt"), cesar_decrypt(content, shift));
		break;
	case 5: // Menu entry: "Exit"
		printf("Exiting program");
		break;
	default: // Invalid option (no menu entry existing for selected option)
		printf("Invalid input - Exiting program");
		return 1;
		break;
	}
	return 0;
}

char *read_file(char *fileName)
{
	FILE *file;
	char *buffer;
	long bytes;

	// Try to open the provided file in "read" mode.
	file = fopen(fileName, "r");
	// if fopen() returns NULL, that means that the file could not be found or accessed.
	if (file == NULL)
	{
		printf("File could not be found!");
		return NULL;
	}
	// We read the amount of bytes the file contains.
	fseek(file, 0, SEEK_END);
	bytes = ftell(file);
	fseek(file, 0, SEEK_SET);
	// And allocate the amount of bytes in the memory.
	buffer = (char *)calloc(bytes, sizeof(char));

	// If the buffer is NULL, that means that an error occurred while allocating the memory (e.g. missing memory)
	if (buffer == NULL)
	{
		printf("An error occurred while allocating the required memory!");
		return NULL;
	}
	// Now we read all bytes from the file into the created buffer.
	fread(buffer, sizeof(char), bytes, file);
	// And close the file after reading it.
	fclose(file);
	return buffer;
}

void write_file(char *fileName, char *content)
{
	// We open the file in "write" mode (which ensures, the file will be created if it does not exist yet)
	FILE *file = fopen(fileName, "w");
	// We write the provided content into the file.
	fprintf(file, "%s", content);
	// And close the file.
	fclose(file);
	// We notify the user where the data was written to.
	printf("Data was written to %s", fileName);
}

int parse_shift_input()
{
	int input;
	printf("Define the shift amount (0-26): ");
	// We read the provided input by the user.
	scanf("%d", &input);
	// And validate it (must be between 0 and 26)
	if (input < 0 || input > 26)
	{
		return -1;
	}
	return input;
}

char *cesar_encrypt(char *input, unsigned int shift)
{
	// create array based on passed shift for replacing the chars
	char secret[26] = "";
	for (int i = 0; i < 26; i++)
	{
		// get new index of specific character with the provided shift
		unsigned int shiftedIndex = i + shift;
		// if the shifted index is out of bounds, we start again at the beginning
		if (shiftedIndex >= 26)
		{
			shiftedIndex = shiftedIndex - 26;
		}
		secret[i] = CHARSET[shiftedIndex];
	}
	// create a dynamic string, so we dont end up in a segfault
	char *toEncrypt = strdup(input);
	// make input lowercase
	toEncrypt = lowercase(toEncrypt);
	// iterate over every character of the input
	for (int i = 0; i < strlen(toEncrypt); i++)
	{
		// We try to find the element of the current character of the string in the defined CHARSET.
		char *element = strchr(CHARSET, toEncrypt[i]);
		// If the pointer is NULL, that means that the current character is not part of the defined CHARSET and can be skipped.
		if (element == NULL)
			continue;
		// Get the index of the current character in the defined CHARSET.
		unsigned int charsetIndex = (int)(element - CHARSET);
		// And change the current character of the string to the shifted version (encrypted).
		toEncrypt[i] = secret[charsetIndex];
	}
	return toEncrypt;
}

char *cesar_decrypt(char *input, int shift)
{
	// create array based on passed shift for replacing the chars
	char secret[26] = "";
	for (int i = 0; i < 26; i++)
	{
		// get new index of specific character with the provided shift
		int shiftedIndex = i - shift;
		// if the shifted index is out of bounds, we start again at the end
		if (shiftedIndex < 0)
		{
			shiftedIndex = shiftedIndex + 26;
		}
		secret[i] = CHARSET[shiftedIndex];
	}
	// create a dynamic string, so we dont end up in a segfault
	char *toDecrypt = strdup(input);
	// make input lowercase
	toDecrypt = lowercase(toDecrypt);
	// iterate over every character of the input
	for (int i = 0; i < strlen(toDecrypt); i++)
	{
		// We try to find the element of the current character of the string in the defined CHARSET.
		char *element = strchr(CHARSET, toDecrypt[i]);
		// If the pointer is NULL, that means that the current character is not part of the defined CHARSET and can be skipped.
		if (element == NULL)
			continue;
		// Get the index of the current character in the defined CHARSET.
		unsigned int charsetIndex = (int)(element - CHARSET);
		// And change the current character of the string to the shifted version (encrypted).
		toDecrypt[i] = secret[charsetIndex];
	}
	return toDecrypt;
}

char *lowercase(char *input)
{
	// We loop every character of the input and try to lowercase it.
	for (int i = 0; input[i]; i++)
	{
		input[i] = tolower(input[i]);
	}
	return input;
}