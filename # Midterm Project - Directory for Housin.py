# Midterm Project - Directory for Undergraduate Housing Issues

class InformationCenter: 
    def __init__(self):
        #Initialize keyword-response directory
        self.response = {
            "phone number": "504-865-5724",
            "hours": "Monday - Friday 8:30 AM - 5 PM",
            "address": "29 McAlister Dr",
            "email": "housing@tulane.edu",
            "rates and housing agreement": "https://housing.tulane.edu/rates-and-housing-agreement",
        }
        
    # Method to retrieve the response to a given keyword 
    def get_response(self, keyword):
        # Check if any other keywords exist in the input
        for key in self.response:
            if keyword in key.lower():
                return self.response[key]
        # If the keyword is not recognized, suggest the availiable options
        return "Keyword not recognized. Please try one of the following: "+", ".join(self.response.keys())

    # Method to add a new keyword and response
    def add_entry(self, keyword, response):
        self.responses[keyword.lower()] = response
        return f"Added '{keyword}' with response: {response}"

class HousingDirectory:
    def __init__(self):
        # Initialize the keyword-response directory
        self.response = {
            "central office": "504-865-5724",
            "central office hours": "Monday - Friday 8:30 AM - 5 PM",
            "weatherhead": "504-865-4120",
            "decou-labat": "504-862-5747",
            "sharp": "504-865-5747",
            "lake": "504-865-6754",
            "greenbaum": "504-865-6802",
            "service wave": "https://servicewave.tulane.edu",
            "mold": "https://servicewave.tulane.edu",
            "plumbing issues": "https://servicewave.tulane.edu",
            "housing office address": "29 McAlister Dr",
            "housing office email adress": "housing@tulane.edu",
        }
        
    # Method to retrieve the response to a given keyword 
    def get_response(self, keyword):
        # Check if any other keywords exist in the input
        for key in self.response:
            if keyword in key.lower():
                return self.response[key]
        # If the keyword is not recognized, suggest the availiable options
        return "Keyword not recognized. Please try one of the following: "+", ".join(self.response.keys())

    # Method to add a new keyword and response
    def add_entry(self, keyword, response):
        self.responses[keyword.lower()] = response
        return f"Added '{keyword}' with response: {response}"

# Main function to choose between functions 
def main():
    # Instantiate both classes 
    info_center = InformationCenter()
    housing_directory = HousingDirectory()
    
    while True:
        # Ask the user which directory they want to interact with
        info = InformationCenter
        housing = HousingDirectory
        directory_choice = input("Which directory would you like to use? (info/housing or 'exit' to quit): ").lower()
        
        # Exit condition
        if directory_choice == 'exit':
            break
        
        # Determine which directory to use 
        if directory_choice == 'info':
            directory = info_center
        elif directory_choice == 'housing':
            directory = housing_directory
        else:
            print("Invalid choice. Please enter 'info' or 'housing'.")
            continue
        
        # Get user input actions within the chosen directory
        while True:
            user_input = input("Enter a keyword (or type 'add' to add entry, 'back' to switch directory, 'exit' to quit):").lower()
            
            if user_input == 'exit':
                return
            
            elif user_input == 'back':
                break
            
            elif user_input == 'add':
                keyword = input("Enter the new keyword: ").lower()
                response = input("Enter the response for the keyword: ")
                print(directory.add_entry(keyword, response))
                
            else:
                print(directory.get_response(user_input))

# Run the main function 
if __name__ == "__main__":
    main()
