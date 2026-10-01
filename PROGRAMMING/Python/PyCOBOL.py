import sys

# The PROCEDURE DIVISION equivalent
def main():
    
    # DATA DIVISION equivalent (Memory Allocation)
    # Python doesn't require strict byte sizing like 'char cust_id[11]', 
    # but we initialize the variable to create the container.
    cust_id = ""
    
    # MOVE "0123456789" TO CUST-ID. (or strcpy in C)
    # Notice we strictly use the underscore here, just like in C.
    cust_id = "0123456789"
    
    # DISPLAY "ID: " CUST-ID. (or printf in C)
    print(f"ID: {cust_id}")
    
    # STOP RUN. (or return 0; in C)
    sys.exit(0)

# This acts as the trigger to run the main logic box
if __name__ == "__main__":
    main()
