"""
1. Blank Receipt
Create a function that prints a blank cash receipt. The function should invoke three other functions: one for printing
the header, one for the body and one for the footer of the receipt.

The header should contain the following text:  CASH RECEIPT
                                               ------------------------------
The body should contain the following text:    Charged to____________________
                                               Received by___________________
And the text for the footer:                   ------------------------------
                                               © SoftUni
"""


def header_print():
    receipt_name = "CASH RECEIPT"
    separator = "------------------------------"
    print(receipt_name)
    print(separator)


def body_print():
    charged_to = "Charged to____________________"
    received_by = "Received by___________________"
    print(charged_to)
    print(received_by)


def footer_print():
    separator = "------------------------------"
    copy_rights = "© SoftUni"
    print(separator)
    print(copy_rights)


def receipt_print():
    header_print()
    body_print()
    footer_print()


receipt_print()