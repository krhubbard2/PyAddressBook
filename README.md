# PyAddressBook
Python developed Address Book for personal project and practice.

## Setup
You will need Python3 and PyQt5 installed on your machine.
Clone this repository to wherever you'd like.
```bash
git clone "https://github.com/krhubbard2/PyAddressBook"
```

## Running
```bash
cd PyAddressBook
python3 pyaddressbook.py
```

## Usage
## First Startup
On first startup (or any case where the sqlite database was deleted) a new file will be created at ./PyAddressBook called "contacts.sqlite". Do not modify this file in any way as it can lead to data corruption.</br> 
When starting up you will be greated with the following:
![](https://i.ibb.co/5vcTYcm/image.png)
### Adding Contacts
Simply click the "Add Contact" button on the top right. You will get this prompt: </br>
![](https://i.ibb.co/41snW8L/image.png)</br>
Name and Email are REQUIRED for all entries. Other fields are optional.
### Deleting Contacts
Simply highlight the row you'd like to delete and click the "Delete" button. You will get a confirmation prompt to confirm you want to delete the entry. Only one entry can be deleted at a time -- highlighting multiple rows to delete will result in undefined behavior.
### Editing Contacts
Simply double click the entry that you would like to edit and change any information you'd like. All edits are saved immediately. 

## Needs Fixing.
The search bar currently does... nothing. I hope to implement a working search function.
