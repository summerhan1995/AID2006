*不需要聚合分组时可以不用group by
show variables like '%sql_mode';
set global sql_mode='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
set session sql_mode='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
1. 查询姓“张”的老师的个数。
select tname,count(tid)  as 个数 from teacher where tname like "张%" group by tname;
2. 查询名字中有“风”字的学生名单。
select sname from student where sname like "%风%";
3. 1990年出生的学生名单（注：student表中sbirth列的类型是datetime）。
select sname,sbirth from student where sbirth REGEXP "^1990";
#筛选用like"1990%" 或者 year(sbirth)=1990
4. 查询课程编号为“02”的总成绩。
select cid as 课程编号,sum(score) as 总成绩 from score where cid=02;
5. 查询选了课程的学生人数。
select count(distinct sid) as 学生人数 from score;
6. 查询各科成绩最高和最低的分： 以如下的形式显示：课程ID，最高分，最低分。
select cid as 课程ID,max(score) as 最高分,min(score) as 最低分
 from score group by cid;
7. 查询每门课程被选修的学生数。
select cid as 课程ID,count(sid) as 学生数 from score group by cid;
8. 查询男生、女生人数。
select ssex,count(sname) as 人数 from student group by ssex;
9. 查询平均成绩大于60分的学生的学号和平均成绩。
select sid as 学号,avg(score) as 平均成绩 from score group by sid having
avg(score)>60;
10. 查询至少选修两门课程的学生学号。
select sid as 学号,count(cid) as 课程数 from score group by sid having
 count(cid)>=2;
11. 查询两门以上不及格课程的同学的学号及其平均成绩。
select sid as 学号 ,avg(score) as 平均成绩 from score where sid in
(select sid from score where score<60 group by sid
 having count(score)>=2) group by sid;
12. 查询同名同姓学生名单并统计同名人数。
select sname,count(sname)from student group by sname
 having count(sname)>=2;
13. 查询每门课程的平均成绩，结果按平均成绩升序排序，平均成绩相同时，按课程号降序排列。
select cid,avg (score) as "平均成绩" from score group by cid
order by avg (score),cid desc ;
14. 查询不及格的课程并按课程号从大到小排列
select cid as 课程号,score as 分数 from score where score < 60 order by cid desc ;
15. 检索课程编号为“04”且分数小于60的学生学号，结果按分数降序排列
select sid,score from score where cid=04 and score<60 order by score desc;
16.统计每门课程的学生选修人数(超过5人的课程才统计)。
要求输出课程号和选修人数，查询结果按人数降序排序，若人数相同，按课程号升序排序。
select cid as 课程ID,count(sid) as 选修人数 from score group by cid having
 count(sid)>5 order by count(sid) desc,cid;
 17. 查询所有课程成绩小于60分的学生的学号、姓名。
select distinct student.sid as 学号,student.sname as 姓名
 from score left join student on
score.sid=student.sid where score <60;
18. 查询没有学全所有课的学生的学号、姓名
select student.sid as 学号,student.sname as 姓名,count(score.cid) as 课程数
from student left join score on
score.sid=student.sid group by student.sid having count(score.cid)<3;
19. 查询出只选修了两门课程的全部学生的学号和姓名。
select student.sid as 学号,student.sname as 姓名,count(cid)
from student left join score on
student.sid=score.sid group by student.sid
having count(cid)=2;
20. 查询课程编号为03且课程成绩在80分以上的学生的学号和姓名
select student.sid as 学号,student.sname as 姓名,score.score
from student left join score on
student.sid=score.sid where cid=03 and
score.score>80;
21. 查询课程编号为“01”的课程比“02”的课程成绩高的所有学生的学号。
select c01.sid as 学号,c01.score as 课程01成绩,c02.score as 课程02成绩
from (select sid,score from score where cid =01
group by sid,score) as c01 left join
(select sid,score from score where cid =02 group by sid,score) as c02
 on c01.sid=c02.sid where c01.score>c02.score;
22. 按平均成绩从高到低，按如下形式显示：学生ID，课程数，平均分。
select sid as 学生ID,count(cid) as 课程数,
avg(score) as 平均分 from score
 group by sid order by avg(score) desc;
23. 使用分段[100-85],[85-70],[70-60],[<60]来统计各科成绩，分别查询各分段的人数、课程ID和课程名称。
select score.cid as 课程ID,course.cname as 课程名称,(CASE when score<60 then 1 else 0 end) as "[<60]",
(CASE when score<70 and score>=60 then 1 else 0 end) as  "[70-60]",
(CASE when score<85 and score>=70 then 1 else 0 end) as  "[85-70]",
(CASE when score<=100 and score>=85 then 1 else 0 end) as  "[100-85]"
from score left join course on score.cid=course.cid;
24. 查询出每门课程的及格人数和不及格人数。
select s01.cid as 课程ID, 及格人数,不及格人数
from (select cid, count(score) as 及格人数
 from score where score >= 60 group by cid) as s01
  left join (select cid, count(score) as 不及格人数
 from score where score < 60 group by cid) as s02 on
 s01.cid=s02.cid;



