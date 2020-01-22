from django.shortcuts import render
from datetime import date
from . import models


# Create your views here.
def home(request):
    """ Handles all actions on the Note Main Page """

    content = {
        'left_header': 'Sites',
    }
    if request.method == 'POST':
        organization = models.Organization.objects.create(name=request.POST['name'],
                                                        street_address=request.POST['street_address'],
                                                        city=request.POST['city'],
                                                        state=request.POST['state'],
                                                        zip_code=request.POST['zip_code'],
                                                        contact_name=request.POST['contact_name'],
                                                        area_code=request.POST['area_code'],
                                                        prefix=request.POST['prefix'],
                                                        line_number=request.POST['line_number'],
        )
        content['organization'] = organization
        return render(request, 'notes/organization.html', content)
    else:
        content['organizations'] = get_organizations()
        return render(request, 'notes/home.html', content)

def organization(request, organization_name):
        content = {
            'organization': get_organization(organization_name),
        }
        if request.method == 'POST':
            site = models.Site.objects.create(name=request.POST['name'],
                                                        street_address=request.POST['street_address'],
                                                        city=request.POST['city'],
                                                        state=request.POST['state'],
                                                        zip_code=request.POST['zip_code'],
                                                        contact_name=request.POST['contact_name'],
                                                        area_code=request.POST['area_code'],
                                                        prefix=request.POST['prefix'],
                                                        line_number=request.POST['line_number'],
                                                        organization=content['organization']
        )
            organization = content['organization']
            content['sites'] = get_sites(organization)
            content['site'] = site
            return render(request, 'notes/site.html', content)
        else:
            organization = content['organization']
            content['sites'] = get_sites(organization)
            return render(request, 'notes/organization.html', content)

def site(request, organization_name, site_name):
    content = {
        'date': str(date.today()),
        'left_header': 'Sites',
        'organization': get_organization(organization_name),
        'site': get_site(site_name),
    }
    if request.method == 'POST':
        new_date = set_date(request.POST['date'])
        note = models.Note.objects.create(date=new_date,
                                        body=request.POST['body'],
                                        site=content['site'],
                                        user=request.user
        )
        organization = content['organization']
        content['sites'] = get_sites(organization)
        site = content['site']
        content['notes'] = get_notes(site)
        return render(request, 'notes/site.html', content)
    else:
        organization = content['organization']
        content['sites'] = get_sites(organization)
        site = content['site']
        content['notes'] = get_notes(site)
        return render(request, 'notes/site.html', content)

def get_organizations():
    """ This function will return all organizations for a User sorted by name. """
    return models.Organization.objects.all().order_by('name')

def get_organization(organization_name):
    """ This function will return data for a given organization. """
    return models.Organization.objects.get(name=organization_name)

def get_sites(organization):
    """ This function will return all site for a User sorted by name. """
    return models.Site.objects.filter(organization_id=organization.id).order_by('name')

def get_site(site_name):
    """ This function will return data for a the site. """
    return models.Site.objects.get(name=site_name)

def get_notes(site):
    """ This function will return all note  data for the site. """
    return models.Note.objects.filter(site_id=site.id).order_by('-date')

def set_date(form_date):
    """ Takes in a date from the form and returns a DateTime object. """
    print(form_date)
    year, month, day = form_date.split("-")
    year = int(year)
    month = int(month)
    day = int(day)
    new_date = date(year, month, day)
    return new_date
