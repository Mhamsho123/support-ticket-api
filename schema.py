from enum import Enum
from pydantic import BaseModel 



class CommentBase(BaseModel):
    author: str
    message: str

class Comment(CommentBase):
    comment_id: int


class CreateComment(CommentBase):
    pass




class TicketPriority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"
    urgent = "urgent"

class TicketStatus(str, Enum):
    open = "open"
    closed = "closed"
    in_progress = "in_progress"
    resolved = "resolved"

class TicketBase(BaseModel):
    title : str
    description: str
    status: TicketStatus
    priority: TicketPriority
    customer_email: str
    assigned_to: str | None = None
    

class Ticket(TicketBase):
    ticket_id: int
    comments: list[Comment]

class CreateTicket(TicketBase):
    pass

class UpdateTicket(BaseModel):
    title : str | None = None
    description: str | None = None
    status: TicketStatus | None = None
    priority: TicketPriority | None = None
    customer_email: str | None = None
    assigned_to: str | None = None


class TicketSummary(BaseModel):
    total: int
    open: int
    in_progress: int
    resolved: int
    closed: int
    urgent: int
    unassigned: int
