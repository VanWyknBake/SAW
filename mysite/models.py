from django.db import models

# HOME SECTION


class Home(models.Model):
    name = models.CharField(max_length=50)
    greetings_1 = models.CharField(max_length=50)
    greetings_2 = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='picture/')
    # save time when modified
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# ABOUT SECTION

class About(models.Model):
    heading = models.CharField(max_length=50)
    career = models.CharField(max_length=50)
    description = models.TextField(blank=False)
    profile_img = models.ImageField(upload_to='profile/')

    updated = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.career


class Profile(models.Model):
    about = models.ForeignKey(About,
                              on_delete=models.CASCADE)
    social_name = models.CharField(max_length=10)
    link = models.URLField(max_length=200)


# SKILLS SECTION

class Category(models.Model):
    name = models.CharField(max_length=20)
    
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name


class Skills(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=20)
    

# PORTFOLIO SECTION

class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio/')
    hovertext = models.CharField(default='By: Player name' ,max_length=50)

    def __str__(self):
        return f'Portfolio {self.id}'


# NEWS

class News(models.Model):
    heading = models.CharField(max_length=50)
    topic = models.CharField(max_length=50)
    description = models.TextField(blank=False)
    img = models.ImageField(upload_to='profile/')

    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.topic

# Squads


class Category2(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Skill2'
        verbose_name_plural = 'Skills2'

    def __str__(self):
        return self.name


class Skills2(models.Model):
    category = models.ForeignKey(Category2,
                                 on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=20)



