class Customer:
    def __init__(self, customer_arrival_data):
        self.arrival_time = customer_arrival_data[0]
        self.service_time = customer_arrival_data[1]
        self.tolerance_time = customer_arrival_data[2]

class Window:
    def __init__(self, index):
        self.is_serving = False
        self.index = index
        self.served = 0
        self.customer = None
        self.time_at_window = 0

def solution(customers, numWindows, queueSize):
    """
    1. find open windows
    2. attend to people at queue aka assign them to open windows
    3. add people to queue. 
    """
    # write your code in Python
    customers = preprocess_customers(customers)
    windows = preprocess_windows(numWindows)
    customer_index = 0
    # print("NUM CUSTOMERS", len(customers))
    num_customers = len(customers)
    curr_time = 0
    queue = [] #fifo so use pop and append
    
    while customers:
        print('CUSTOMERS', len(customers))
        print("CURR TIME", curr_time)
        output = [i.served for i in windows]
        # print("OUTPUT1", output)
        # output_with_total = output.insert
        # print("OUTPUT2", output_with_total)
        output.insert(0, sum(output))
        print(output)
        open_windows = []
        for window in windows:
            print("a")
            if window.is_serving:
                customer = window.customer
                time_at_window = window.time_at_window
                if customer.service_time == time_at_window:

                    window.is_serving = False
                    window.customer = None
                    window.time_at_window = 0
                    # queue.remove([customer, time])
                    
                    #this window is now available.
                    open_windows.append(window)
                
            else:
                #add window to open windows list
                open_windows.append(window)

        print("OPEN WINDOWS", [i.index for i in open_windows])
                
        for c in queue:
            customer = c[0]
            time_in_queue = c[1]
            print("b")
            print("CUSTOMERS IN QUEUE", [i[0].arrival_time for i in queue])
            if time_in_queue > customer.tolerance_time:
                print("abc")
                queue.remove(c)
            if open_windows:
                print("abcd")
                print("customer   ", customer.arrival_time, " assigned to window:", open_windows[0].index)
                open_window = open_windows[0]
                
            
                open_window.is_serving = True
                open_window.customer = customer

                print("which window was it assigned", open_window.index)
                open_windows.remove(open_window)
                print([i.index for i in open_windows])
                queue.remove(c)

                open_window.served += 1
                if customer in customers:
                    customers.remove(customer)





        while is_room_in_queue(queue, queueSize):
            print("c")
            print("CUSTOMERS IN QUEUE", [i[0].arrival_time for i in queue])
            print(curr_time)
            next_customer = customers[0]
            print(next_customer.arrival_time)
            if next_customer.arrival_time == curr_time:
                customer_in_queue = [next_customer, 0]
                queue.append(customer_in_queue)
                customers.remove(next_customer)
                if len(customers) == 0:
                    break
            if next_customer.arrival_time < curr_time:
                customers.remove(next_customer)
            else:
                break

        print("CUSTOMERS IN QUEUE", [i[0].arrival_time for i in queue])

        while (open_windows and queue):
            print("d")
            print("open windows and queue")
            next_customer, wait_time = queue[0]
            print("wait time", wait_time)
            print("tolerance tiem", next_customer.tolerance_time)
            open_window = open_windows[0]
            print("THIS IS THE WINDOW", open_window.index)
            if curr_time == next_customer.arrival_time:
                print("here1")   
                if wait_time <= next_customer.tolerance_time:
                    open_window.is_serving = True
                    open_window.customer = next_customer
                    open_window.served += 1
                    del queue[0]
                    print("here2")
            if curr_time == next_customer.arrival_time and not open_windows:
                if next_customer in customers:
                    customers.remove(next_customer)
                    # del queue[0]
            else:
                break

        if queueSize == 0 and customers:
            # print(len(customers))
            next_customer = customers[0]
            if curr_time == next_customer.arrival_time and open_windows:
                open_window = open_windows[0]

                open_window.is_serving = True
                open_window.customer = next_customer
                open_window.served += 1
                customers.remove(next_customer)
            if curr_time == next_customer.arrival_time and not open_windows:
                customers.remove(next_customer)




        
    
        curr_time += 1
        for customer in queue:
            customer[1] += 1
            
        for window in windows:
            window.time_at_window += 1
        if curr_time == 126:
            return

    output = [i.served for i in windows]
    output.insert(0, sum(output))
    return output
    
def preprocess_customers(customers):
    output_customers = []
    for i in range(len(customers)):
        # print(type(customers[i]))
        customer_string = customers[i]
        
        data = customer_string.split(',')
        customer_arrival_ints = [int(data[0]),int(data[1]), int(data[2])]
        customer = Customer(customer_arrival_ints)
        output_customers.append(customer)
    return output_customers
    

def preprocess_windows(numWindows):
    output_windows = []
    for i in range(numWindows):
        window = Window(i+1)
        output_windows.append(window)
    return output_windows

def is_room_in_queue(queue, queueSize):
    if len(queue) < queueSize:
        return True
    else:
        return False
    


customers = ['0,25,600', '5,20,600', '10,20,8', '15,50,100', '20,100,20']
print(solution(customers, 2, 1))







