import math

class MessageCoder:
    def __init__(self, key):
        self.key = key

    def encrypt_message(self, message):
        
        message = message.replace(" ", "")
        message_length = len(message)
        num_rows = math.ceil(message_length / self.key)

        encrypted_message = ""

        for col in range(self.key):
            for row in range(num_rows):
            
                index = col + (row * self.key)
                
            
                if index < message_length:
                    encrypted_message += message[index]

    
        return encrypted_message

    def decrypt_message(self, message):
        message_split = list(message)


        message_length = len(message_split)

    
        message_ceil = math.ceil(message_length / self.key)

    
        total_cells = self.key * message_ceil
        num_empty_cells = total_cells - message_length

        
        message_grid = [[''] * message_ceil for _ in range(self.key)]


        iterator = iter(message_split)


        for col in range(message_ceil):
            for row in range(self.key):
        
                if col == message_ceil - 1 and row >= self.key - num_empty_cells:
                    continue
                message_grid[row][col] = next(iterator)

        
        message_decrypted = ''


        for row in message_grid:
            message_decrypted += ''.join(row)

        
        return message_decrypted


encrypted_message = "khushi"
value = MessageCoder(11)
decrypted_message = value.decrypt_message(encrypted_message)
print(decrypted_message)  

