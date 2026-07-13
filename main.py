from fastapi import FastAPI

app = FastAPI()


tickets = [
    {
        "ticket_id": 1,
        "title": "Cannot log in",
        "description": "The password reset email never arrives.",
        "status": "open",
        "priority": "high",
        "customer_email": "sarah@example.com",
        "assigned_to": None,
        "comments": [
            {
                "comment_id": 1,
                "author": "Support Bot",
                "message": "Your ticket has been received."
            }
        ]
    },
    {
        "ticket_id": 2,
        "title": "Payment charged twice",
        "description": "The customer was charged twice for the same order.",
        "status": "in_progress",
        "priority": "urgent",
        "customer_email": "michael@example.com",
        "assigned_to": "Amanda",
        "comments": [
            {
                "comment_id": 1,
                "author": "Amanda",
                "message": "I am reviewing the payment records."
            },
            {
                "comment_id": 2,
                "author": "Michael",
                "message": "I can provide screenshots if needed."
            }
        ]
    },
    {
        "ticket_id": 3,
        "title": "Profile picture will not upload",
        "description": "Uploading a PNG image produces an error.",
        "status": "resolved",
        "priority": "medium",
        "customer_email": "layla@example.com",
        "assigned_to": "David",
        "comments": [
            {
                "comment_id": 1,
                "author": "David",
                "message": "The uploaded image was larger than the allowed size."
            },
            {
                "comment_id": 2,
                "author": "Layla",
                "message": "Compressing the image fixed the problem."
            }
        ]
    },
    {
        "ticket_id": 4,
        "title": "Feature request for dark mode",
        "description": "The customer wants a dark theme for the dashboard.",
        "status": "closed",
        "priority": "low",
        "customer_email": "omar@example.com",
        "assigned_to": None,
        "comments": []
    }
]