# Generated by Django 2.2 on 2019-05-06 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subject_Code', models.CharField(max_length=255)),
                ('Course_Number', models.CharField(max_length=255)),
                ('Course_Name', models.CharField(max_length=255)),
                ('Credit_Hours', models.PositiveIntegerField(default=0)),
                ('Description', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'Course',
            },
        ),
        migrations.CreateModel(
            name='CourseSection',
            fields=[
                ('Section_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Year', models.PositiveIntegerField(default=0)),
                ('Semester', models.CharField(choices=[('SP', 'Spring semester'), ('SM', 'Summer semester'), ('FA', 'fall semester'), ('WI', 'winter semester')], max_length=255)),
                ('Enrollment', models.CharField(max_length=255)),
                ('Comment1', models.CharField(max_length=255)),
                ('Comment2', models.CharField(max_length=255)),
                ('Associated_Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Curriculum.Course')),
            ],
            options={
                'db_table': 'CourseSection',
            },
        ),
        migrations.CreateModel(
            name='CourseTopics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Associated_Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Curriculum.Course')),
            ],
            options={
                'db_table': 'CourseTopics',
            },
        ),
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cur_name', models.CharField(max_length=255)),
                ('Min_Hours', models.PositiveIntegerField(default=0)),
                ('Topic_Category', models.CharField(choices=[('EX', 'Extensive'), ('IN', 'Inclusive'), ('BP', 'BasicPlus'), ('BC', 'Basic'), ('US', 'Unsatisfactory'), ('SB', 'Substandard')], default='BC', max_length=255)),
            ],
            options={
                'db_table': 'Curriculum',
            },
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Description', models.CharField(max_length=255)),
                ('Associated_Curriculum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Curriculum.Curriculum')),
            ],
            options={
                'db_table': 'Goal',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'Person',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'Topic',
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('Grade_Distribution_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Letter_Grade', models.CharField(choices=[('A+', 'A+'), ('A', 'A'), ('A-', 'A-'), ('B+', 'B+'), ('B', 'B'), ('B-', 'B-'), ('C+', 'C+'), ('C', 'C'), ('C-', 'C-'), ('D+', 'D+'), ('D', 'D'), ('D-', 'D-'), ('F', 'Fail'), ('W', 'Withdraw'), ('I', 'Incomplete')], max_length=255)),
                ('dist_number', models.IntegerField(default=0)),
                ('Associated_Course_Section', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Curriculum.CourseSection')),
                ('Associated_Goal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Curriculum.Goal')),
            ],
            options={
                'db_table': 'Grade',
            },
        ),
        migrations.CreateModel(
            name='CurriculumTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Level', models.PositiveIntegerField(choices=[(1, 'Level 1'), (2, 'Level 2'), (3, 'Level 3')], default=1)),
                ('Subject_Area', models.CharField(max_length=255)),
                ('Units', models.PositiveIntegerField(default=0)),
                ('Associated_Curriculum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Curriculum.Curriculum')),
                ('Associated_Topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Curriculum.CourseTopics')),
            ],
            options={
                'db_table': 'CurriculumTopic',
            },
        ),
        migrations.CreateModel(
            name='CurriculumCT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Units', models.PositiveIntegerField(default=0)),
                ('Associated_CT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Curriculum.CourseTopics')),
                ('Associated_Curriculum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Curriculum.Curriculum')),
            ],
            options={
                'db_table': 'CurriculumCT',
            },
        ),
        migrations.CreateModel(
            name='CurriculumCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Required', models.BooleanField()),
                ('Associated_Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Curriculum.Course')),
                ('Associated_Curriculum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Curriculum.Curriculum')),
            ],
            options={
                'db_table': 'CurriculumCourse',
            },
        ),
        migrations.AddField(
            model_name='curriculum',
            name='Head',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Curriculum.Person'),
        ),
        migrations.AddField(
            model_name='coursetopics',
            name='Associated_Topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Curriculum.Topic'),
        ),
        migrations.CreateModel(
            name='CourseGoal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Associated_Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Curriculum.Course')),
                ('Associated_Goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Curriculum.Goal')),
            ],
            options={
                'db_table': 'CourseGoal',
            },
        ),
        migrations.AddConstraint(
            model_name='course',
            constraint=models.UniqueConstraint(fields=('Subject_Code', 'Course_Number'), name='course_unique'),
        ),
        migrations.AddConstraint(
            model_name='curriculumtopic',
            constraint=models.UniqueConstraint(fields=('Associated_Curriculum', 'Associated_Topic'), name='currTopic_unique'),
        ),
        migrations.AddConstraint(
            model_name='curriculumct',
            constraint=models.UniqueConstraint(fields=('Associated_Curriculum', 'Associated_CT'), name='CCT_Unique'),
        ),
        migrations.AddConstraint(
            model_name='curriculumcourse',
            constraint=models.UniqueConstraint(fields=('Associated_Curriculum', 'Associated_Course'), name='curriculumCourse_unique'),
        ),
        migrations.AddConstraint(
            model_name='curriculum',
            constraint=models.UniqueConstraint(fields=('Cur_name',), name='curriculum_unique'),
        ),
        migrations.AddConstraint(
            model_name='coursetopics',
            constraint=models.UniqueConstraint(fields=('Associated_Course', 'Associated_Topic'), name='courseTopics_unique'),
        ),
        migrations.AddConstraint(
            model_name='coursesection',
            constraint=models.UniqueConstraint(fields=('Section_ID', 'Associated_Course', 'Year', 'Semester'), name='courseSection_unique'),
        ),
        migrations.AddConstraint(
            model_name='coursegoal',
            constraint=models.UniqueConstraint(fields=('Associated_Goal', 'Associated_Course'), name='courseGoal_unique'),
        ),
    ]
