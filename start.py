# -*- coding: utf-8 -*-
from flask import (Flask, render_template, request, url_for, redirect)
from apis import (sl, chuck, time, Weather, Debaser,nasa,appSecretKey)
from decimal import Decimal
from dbModels import TimmieHome , db, Migrate, app
from forms import TimmieForm
from sqlalchemy import desc


# app route ex '/' will be the root ex timmieonline.com '/hi'  = timmienilsson.com/hi
@app.route('/', methods = ['GET', 'POST'])
def index():
    #iniate a form
    form = TimmieForm()

    # If forn is valid do things
    if form.validate_on_submit():
        home_or_not = form.timmiehome.data
        if home_or_not == 'True':
            home_or_not = True
        else:
            home_or_not = False

        ishome = TimmieHome(home_or_not)
        db.session.add(ishome)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        print(form.errors)
    #Database request below
    isTimmieHome = TimmieHome.query.all()
    if str(isTimmieHome) != '[]':
        isTimmieHome = isTimmieHome[-1]
    else:
        isTimmieHome = 'Ingen vet vart Timmie ar nu :-O'
    #Here im iniiating all the variables with infor from the API
    debaser = Debaser()
    weather = Weather()
    timedate = time()
    sls = sl()
    chuckJoke = chuck()
    nasaPic = nasa()
    # Here ins jinja2 rendering all the things into html
    return render_template('index.html', debaser = debaser, weather = weather,
                            timedate = timedate, sls = sls, chuckJoke = chuckJoke,
                            nasaPic = nasaPic, form = form, isTimmieHome = isTimmieHome)

if __name__ == '__main__':
    app.run(debug = True)
