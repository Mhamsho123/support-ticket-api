from fastapi import FastAPI, HTTPException 
from schema import CreateComment, CreateTicket, Ticket, UpdateTicket, Comment

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


@app.get("/tickets", response_model=list[Ticket])
async def get_tickets():
    return tickets

@app.get("/tickets/{tickets_id}", response_model=Ticket)
async def get_single_ticket(tickets_id: int):
    for ticket in tickets:
        if ticket.get("ticket_id") == tickets_id:
            return ticket
    raise HTTPException(status_code=404, detail="Couldn't find the ID")


@app.post("/tickets", status_code=201,response_model= Ticket)
async def create_ticket(create_ticket: CreateTicket):
    new_id = max((ticket.get("ticket_id") for ticket in tickets), default=0) +1
    new_post = {
        "ticket_id": new_id,
        **create_ticket.model_dump(mode="json"),
        "comments": []
    }

    tickets.append(new_post)

    return new_post


@app.patch("/tickets/{tickets_id}", response_model = Ticket)
async def update_ticket(tickets_id: int, update: UpdateTicket):
    for ticket in tickets:
        if ticket.get("ticket_id") == tickets_id:
            update_data = update.model_dump(exlude_unset=True, mode="json")
            
            ticket.update(update_data)
            return ticket
    raise HTTPException(status_code=404, detail="Couldn't find the ID")


@app.delete("/tickets/{ticket_id}", response_model=Ticket)
async def delete_ticket(ticket_id: int):
    for ticket in tickets:
        if ticket.get("ticket_id") == ticket_id:
            tickets.remove(ticket)
            return ticket
    raise HTTPException(status_code=404, detail="Couldn't find the ID")

        


@app.post(
    "/tickets/{ticket_id}/comments",
    status_code=201,
    response_model=Comment
)
async def create_comment(ticket_id: int, add_comment: CreateComment):
    for ticket in tickets:
        if ticket.get("ticket_id") == ticket_id:
            comments = ticket["comments"]

            new_comment_id = max(
                (comment["comment_id"] for comment in comments),
                default=0
            ) + 1

            new_comment = {
                "comment_id": new_comment_id,
                **add_comment.model_dump(mode="json")
            }

            comments.append(new_comment)

            return new_comment

    raise HTTPException(
        status_code=404,
        detail="Couldn't find the ticket"
    )
