from django.shortcuts import redirect, render
from datetime import date
from . import forms, models
from walktest.models import WalkTest


# Create your views here.
def home(request):
    """ Handles all actions on the Note Main Page """

    content = {
        'left_header': 'Organizations',
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
            'left_header': 'Sites',
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
    content['walktests'] = WalkTest.objects.filter(site=content['site'])
    if request.method == 'POST':
        organization = content['organization']
        content['sites'] = get_sites(organization)
        site = content['site']
        form = forms.NoteForm(request.POST)
        content['form'] = form
        if form.is_valid():
            models.Note.objects.create(date=form.cleaned_data['date'],
                                            body=form.cleaned_data['body'],
                                            site=content['site'],
                                            user=request.user
            )

            content['notes'] = get_notes(site)
            return render(request, 'notes/site.html', content)
        else:
            return render(request, 'notes/site.html', content)
    else:
        organization = content['organization']
        content['sites'] = get_sites(organization)
        site = content['site']
        content['notes'] = get_notes(site)
        content['form'] = forms.NoteForm()
        return render(request, 'notes/site.html', content)

def org_search(request):
    """ Handles a search for any organizations that match the users search. """

    content = {
        'left_header': 'Organizations',
        'organizations': get_organizations()
    }
    if request.method == 'POST':
        search = request.POST['search_text']
        content['org_search_results'] = models.Organization.objects.filter(name=search)
        return render(request, 'notes/org_search.html', content)
    else:
        return redirect('notes-home')


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

def set_date(year, month, day):
    """ Takes in a date from the form and returns a DateTime object. """
    new_date = date(year, month, day)
    return new_date
