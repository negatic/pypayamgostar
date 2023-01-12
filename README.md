# Quickstart
this is a simple package to interact with your payamgostar crm webservices through python.
all you have to do to start is to create a new Pypg object and use it to interact with your webservices:
```python
payamgostar = Pypg(url='example_url.com',username='yourusername',password='yourpassword')
# Example: How to Delete a Person
payamgostar.Person.delete(PersonId=1)
```
## Installing
After finalizing the first version the package will be officially published on the python package manager 
```
pip install pypayamgostar
```