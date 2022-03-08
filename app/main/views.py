from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import PitchForm,UpdateProfile, CommentForm
from ..models import User,Pitch,Comment
from flask_login import login_required, current_user
from .. import db,photos

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to The best Pitching Website'

    # Getting reviews by category
    interview_pich = Pitch.get_pitches('interview')
    product_pich = Pitch.get_pitches('product')
    promotion_pitch = Pitch.get_pitches('promotion')


    return render_template('index.html',title = title, interview = interview_pich, product = product_pich, promotion = promotion_pitch)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    pitch_count = Pitch.pitch_number(uname)

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user, pitch = pitch_count)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():

        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path

        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


@main.route('/pitches/interview_pitch')
def interview_pitch():

    pitch = Pitch.get_pitches('interview')

    return render_template("interview_pitch.html", pitch = pitch)

@main.route('/pitches/product_pitch')
def product_pitch():

    pitch = Pitch.get_pitches('product')

    return render_template("product_pitch.html", pitch = pitch)

@main.route('/pitches/promotion_pitch')
def promotion_pitch():

    pitch = Pitch.get_pitches('promotion')

    return render_template("promotion_pitch.html", pitch = pitch)

@main.route('/pitch/<int:id>', methods = ['GET','POST'])
def pitch(id):
    pitch = Pitch.get_pitch(id)

    if request.args.get("like"):
        pitch.likes = pitch.likes + 1

        db.session.add(pitch)
        db.session.commit()

        return redirect("/pitch/{pitch_id}".format(pitch_id=pitch.id))

    elif request.args.get("dislike"):
        pitch.dislikes = pitch.dislikes + 1

        db.session.add(pitch)
        db.session.commit()

        return redirect("/pitch/{pitch_id}".format(pitch_id=pitch.id))

    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        comment = comment_form.text.data

        new_comment = Comment(comment = comment,user = current_user,pitch_id = pitch)

        new_comment.save_comment()


    comments = Comment.get_comments(pitch)

    return render_template("pitch.html", pitch = pitch, comment_form = comment_form, comments = comments)

@main.route('/user/<uname>/pitch')
def user_pitch(uname):
    user = User.query.filter_by(username=uname).first()
    pitch = Pitch.query.filter_by(user_id = user.id).all()
    pitch_count = Pitch.pitch_number(uname)

    return render_template("profile/pitch.html", user=user, pitch=pitch, pitch_count=pitch_count)



@main.route('/pitch/new', methods = ['GET','POST'])
@login_required
def new_pitch():
    pitch_form = PitchForm()
    if pitch_form.validate_on_submit():
        title = pitch_form.title.data
        pitch = pitch_form.text.data
        category = pitch_form.category.data

        # Updating the pitch instance
        new_pitch = Pitch(pitch_title=title,pitch_content=pitch,category=category,user=current_user,likes=0,dislikes=0)

        # Saving the pitch method
        new_pitch.save_pitch()
        return redirect(url_for('.index'))
    title = f''
    return render_template('new_pitch.html',title = title,pitch_form=pitch_form )