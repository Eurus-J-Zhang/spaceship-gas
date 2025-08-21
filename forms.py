from flask_wtf import FlaskForm
from wtforms import RadioField, StringField, IntegerField
from wtforms.validators import DataRequired, NumberRange
from wtforms.widgets import TextArea

# Prolific ID and gender and age
class DemographicInfo(FlaskForm):
    id = StringField('Prolific ID', validators=[DataRequired()])
    gender = RadioField('Gender', choices=[('M','Male'),('F','Female'),('O','Others')], validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=18, max=80)])

eleven_point_scale = [(str(i), f'Opt{i}') for i in range(11)]


# tank check
class TankForm(FlaskForm):
    tank_practice = RadioField('Practice', choices=[('A','A. Increase oxygen by 1%'),('B','B. Decrease oxygen by 1%'),
                                                    ('C','C. Increase carbon dioxide by 0.2%'),('D','D. Decrease carbon dioxide by 0.2%')], validators=[DataRequired()])

# tank reason
class ReasonForm(FlaskForm):
    tank_reason = RadioField('Reason', choices=[('A','A. Close Loop (O₂+0.5, CO₂+0.5)'),
                                                ('B','B. Vent (O₂−0.5, CO₂−0.5)'),
                                                ('C','C. Inject & Scrub (O₂+1, CO₂−1)'),
                                                ('D','D. Recycle (O₂−1, CO₂+1)')], validators=[DataRequired()])


# Emotion check
class EmotionForm(FlaskForm):
    despair = RadioField('Despair', choices=eleven_point_scale, validators=[DataRequired()])
    anxiety = RadioField('Anxiety', choices=eleven_point_scale, validators=[DataRequired()])
    irritation = RadioField('Irritation', choices=eleven_point_scale, validators=[DataRequired()])
    rage = RadioField('Rage', choices=eleven_point_scale, validators=[DataRequired()])
    shame = RadioField('Shame', choices=eleven_point_scale, validators=[DataRequired()]) 
    guilt = RadioField('Guilt', choices=eleven_point_scale, validators=[DataRequired()])  
    
    feedback = StringField('',validators=[DataRequired()],widget=TextArea())

# Appraisal Check
class AppraisalForm(FlaskForm):
    agent = RadioField('Agent', choices=[('Nature','Nature'),('Others','Another crew member'),('Self','Yourself')], validators=[DataRequired()])
    power = RadioField('Power', choices=[('Y','Yes'),('N','No')], validators=[DataRequired()])