from django.db import models

from apps.core.models import TimeStampedModel


class Team(TimeStampedModel):
    name = models.CharField(verbose_name='team', max_length=128, db_index=True)  # noqa: WPS432

    def __str__(self):
        return self.name


class Column(TimeStampedModel):
    team = models.ForeignKey(Team, verbose_name='team', related_name='columns', related_query_name='column', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='name', max_length=128, db_index=True)  # noqa: WPS432
    color = models.CharField(verbose_name='color', max_length=7, default='#dee2e6')  # noqa: WPS432
    index = models.IntegerField(verbose_name='index')

    class Meta:
        unique_together = ('team', 'name', 'index')

    def __str__(self):
        return self.name


class ColumnLabel(TimeStampedModel):
    column = models.ForeignKey(Column, verbose_name='column', related_name='labels', related_query_name='label', on_delete=models.CASCADE)
    gitlab_label_id = models.IntegerField(verbose_name='gitlab label id', db_index=True)


class Project(TimeStampedModel):
    team = models.ForeignKey(Team, verbose_name='project', related_name='projects', related_query_name='project', on_delete=models.CASCADE)
    gitlab_project_id = models.IntegerField(verbose_name='gitlab project id', db_index=True)

    class Meta:
        unique_together = ('team', 'gitlab_project_id')
