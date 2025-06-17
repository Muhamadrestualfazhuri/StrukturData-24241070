class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self, capacity):
        self.top = None
        self.capacity = capacity
        self.size = 0

    def push(self, data):
        if self.is_full():
            print("Stack sudah penuh!")
            return
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
        print(f"Stack: {self.display()}")

    def pop(self):
        if self.is_empty():
            print("Stack kosong!")
            return None
        popped_node = self.top
        self.top = self.top.next
        self.size -= 1
        return popped_node.data

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def peek(self):
        if self.is_empty():
            print("Stack kosong!")
            return None
        return self.top.data

    def display(self):
        current = self.top
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        elements.reverse()
        return elements

    def get_size(self):
        return self.size

def main():
    print("=====PROGRAM SEDERHANA UNTUK IMPLEMENTASI STACK DENGAN LINKED-LIST=====")
    capacity = int(input("Tentukan berapa kapasitas stack: "))
    stack = Stack(capacity)

    while True:
        print("\nPilih menu berikut ini:")
        print("1. Menambah isi stack")
        print("2. Menghapus isi stack")
        print("3. Cek Ukuran Stack saat ini")
        print("4. Cek Puncak Stack")
        print("5. Cek Stack Full")
        print("6. Keluar 🔚")
        
        choice = int(input("Masukkan pilihan anda: "))
        
        if choice == 1:
            data = int(input("Masukkan isi stack: "))
            stack.push(data)
            while True:
                tambah = input("Menambah isi Stack Pilih [Ya/Tidak]: ").lower()
                if tambah == 'ya':
                    data = int(input("Masukkan isi stack: "))
                    stack.push(data)
                elif tambah == 'tidak':
                    break
                else:
                    print("Input tidak valid, silakan ketik Ya atau Tidak.")

        elif choice == 2:
            popped_value = stack.pop()
            if popped_value is not None:
                print(f"Elemen yang dihapus: {popped_value}")
            print(f"Stack setelah dihapus: {stack.display()}")

        elif choice == 3:
            print(f"Ukuran Stack saat ini: {stack.get_size()}")

        elif choice == 4:
            top_value = stack.peek()
            if top_value is not None:
                print(f"Puncak Stack: {top_value}")

        elif choice == 5:
            if stack.is_full():
                print("Stack dalam kondisi penuh.")
            else:
                print("Stack tidak penuh.")

        elif choice == 6:
            print("Good work! (⌐■_■).")
            break

        else:
            print("Pilihan tidak valid. pilih opsi 1 sampai 6")

if __name__ == "__main__":
    main()