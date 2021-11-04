from flask import Flask, render_template, url_for, request, redirect
import os
from lib import Agent, Client, Company, Listing


app = Flask(__name__)

@app.route("/")
def home():
    return "Home page"

@app.route("/listing")
def listing_search():
    """Renders the template to search for listings

    Returns:
        rendered html template
    """

    return render_template("listing_search.html")

@app.route("/listing/<listing_id>")
def listing_view(listing_id: str):
    """Renders the template for a listing

    Args:
        listing_id (str): The listing to render

    Returns:
        rendered html template
    """
    try: 
        listing_id = int(listing_id)
    except ValueError:
        return "Invalid listing id" #Probaby substitute with a 404 page
    

    listing = Listing.from_listing_id(listing_id)
    agent = Agent.from_license_number(listing.agent_license_number)

    return render_template("listing.html", listing=listing, agent=agent)

@app.route("/agent/<agent_id>")
def agent(agent_id):
    """Renders the template for an agent

    Args:
        agent_id (str): the agent to render for

    Returns:
        rendered html template
    """

    try: 
        agent_id = int(agent_id)
    except ValueError:
        return "Invalid agent id" #Probaby substitute with a 404 page
    
    agent = Agent.from_license_number(agent_id)
    company = Company.from_company_id(agent.company_id)

    return render_template("agent.html", agent=agent, company=company)

@app.route("/client/<client_id>")
def client(client_id: str):
    """Renders the template for a client

    Args:
        client_id (str): the client to render for

    Returns:
        rendered html template
    """

    try:
        client_id = int(client_id)
    except ValueError:
        return "Invalid client id" #Probaby substitute with a 404 page
    
    client = Client.from_client_id(client_id)
    return render_template("client.html", client=client)

@app.route("/company/<company_id>")
def company(company_id: str):
    """Renders the template for a company

    Args:
        company_id (str): the company to render for

    Returns:
        rendered html template
    """        

    try: 
        company_id = int(company_id)
    except ValueError:
        return "Invalid company id" #Probaby substitute with a 404 page
    
    company = Company.from_company_id(company_id)

    return render_template("company.html", company=company) #TODO doesn't exist yet

@app.route("/add_listing", methods=["GET", "POST"])
def add_listing():
    """Renders the template to add a listing

    Returns:
        rendered html template
    """

    if request.method == "POST": #if they're adding a listing
        req = request.form

        return redirect(request.url)

    return render_template("add_listing.html") #They're just viewing the form


if __name__ == "__main__":
    app.run()
