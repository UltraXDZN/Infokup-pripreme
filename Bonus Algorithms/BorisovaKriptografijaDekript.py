message = input()

num_sections = len(message) // 4

decrypted_message = ""
for i in range(num_sections):
    decrypted_message += message[i::num_sections]

print(decrypted_message.replace("X", ""))