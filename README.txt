Welcome to my Python Project!

----> About <----
This series of scripts is meant to connect to an organization's ldap, perform a search for user objects, and deliver those objects to a dictionary(?)

the dictionary will output to an xml file with special tags/formatting that work with the "My Learning Plan" application.

----> Goal <----
Eventually I would like to build this into a windows virtual machine that will act as a synchronization hub between a local ldap and MLP's upload url.  This series of scripts will turn into an application that can check against past work done, and be smart about keeping user data current.

The focus should be on dealing with exceptions that might arrise while running the application in production.