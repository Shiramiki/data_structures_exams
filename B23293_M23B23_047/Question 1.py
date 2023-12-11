class BrowserStack:
    def __init__(self):
        # Initialize the browser with empty lists for next, back, and a current page
        self.next = []
        self.back = []
        self.current = None
        
    def navigation(self, url):
        # Navigate to a new URL
        if self.current is None:
            # If there is no current page, set the current page to the new URL
            self.current = url
        else:
            # If there is a current page, move it to the back stack and set the new URL as the current page
            self.back.append(self.current)
            self.current = url
            # Clear the forward stack
            self.next = []
        # Return the current page
        return self.current
    
    def backward(self):
        # Move backward in the browsing history
        if self.back:
            # If there are pages in the back stack, move the current page to the forward stack and set the previous page as the current page
            self.next.append(self.current)
            self.current = self.back.pop()
            print(self.current)
        else:
            # If there are no pages in the back stack, print a message indicating no more pages
            print("No more pages")
    
    def forward(self):
        # Move forward in the browsing history
        if self.next:
            # If there are pages in the forward stack, move the current page to the back stack and set the next page as the current page
            self.back.append(self.current)
            self.current = self.next.pop()
            print(self.current)
        else:
            # If there are no pages in the forward stack, print a message indicating no more pages
            print("No more pages")

# Example usage of the BrowserStack class
browser = BrowserStack()
pages = ["www.google.com", "www.github.com", "www.github.com", "www.yahoo.com", "www.ucu.com", "www.microsoft.com", "www.skype.com"]
for page in pages:
    browser.navigation(page)
    
browser.backward()
browser.backward()
browser.forward()
browser.navigation("www.w3schools.com")
browser.forward()

# This is the output of the code
# www.microsoft.com
# www.ucu.com
# www.microsoft.com
# No more pages