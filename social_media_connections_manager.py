import networkx as nx 
import matplotlib.pyplot as plt 
 
class ConnectionsManager: 
    def __init__(self): 
        self.graph = nx.Graph() 
         
    def add_user(self, username): 
        self.graph.add_node(username) 
        print(f"User '{username}' has been added") 
               
               
    def add_connection(self, user1, user2): 
        if user1 and user2 in self.graph: 
            self.graph.add_edge(user1, user2) 
            print(f"Connection created between '{user1}' and '{user2}'") 
        else: 
            print("Both users must exist for the connection to be created.") 
             
     
    def view_all_users(self): 
        users = list(self.graph.nodes()) 
        if users: 
            print("All Users:") 
            for user in users: 
                print(f"- {user}") 
        else: 
            print("No users found!") 
             
             
    def view_all_connections(self): 
        connections = list(self.graph.edges()) 
        if connections: 
            print("All Connections:") 
            for conn in connections: 
                print(f"- {conn[0]} <-> {conn[1]}") 
        else: 
            print("No connections available!") 
             
             
    def display_graph(self): 
        plt.figure(figure=(8, 6)) 
        nx.draw(self.graph, with_labels=True, node_color='lightgreen', 
node_size=2000, font_color='black', font_weight='bold', edge_color='gray') 
        plt.title("Social Media Connections") 
        plt.show() 
         
         
class MainMenu: 
    def __init__(self): 
        self.manager = ConnectionsManager() 
         
         
    def display_menu(self): 
        while True: 
            print("\n Social Media Connections Manager") 
            print("1. Add User") 
            print("2. Add Connection") 
            print("3. View All Users") 
            print("4. View All Connections") 
            print("5. Display Graph") 
            print("6. Exit") 
            choice = input("Select an option: ") 
             
             
            if choice == '1': 
                self.add_user() 
            elif choice == '2': 
                self.add_connections() 
            elif choice == '3': 
                self.manager.view_all_users() 
            elif choice == '4': 
                self.manager.view_all_connections() 
            elif choice == '5': 
                self.manager.display_graph() 
            elif choice == '6': 
                print("Exiting the application") 
                break 
            else: 
                print("Invalid option! Please try again") 
                 
                 
    def add_user(self): 
        username = input("Enter the username to add: ") 
        self.manager.add_user(username) 
         
         
def add_connections(self): 
user1 = input("Enter the name of the first user: ") 
user2 = input("Enter the name of the second user: ") 
self.manager.add_connection(user1, user2) 
if __name__ == "__main__": 
menu = MainMenu() 
menu.display_menu()