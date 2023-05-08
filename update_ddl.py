#!/usr/bin/python3

import yaml
from pathlib import Path


if __name__ == "__main__":
    root_path = Path(__file__).absolute().parent
    ddl_path = root_path.joinpath('ddl.md')
    conference_path = root_path.joinpath('conference')

    file_title = '会议截稿时间'
    table = ['| 会议 | 截稿日期 | 时间 | 地点 | 网址 |', '| --- | --- | --- | --- | --- |']
    for conference in conference_path.iterdir():
        if data := yaml.load(conference.read_text(), Loader=yaml.FullLoader):
            title = data[0]['title']
            conf = data[0]['confs'][-1]
            year = conf['year']
            deadline = conf['timeline'][-1]['deadline']
            timezone = conf['timezone']
            date = conf['date']
            place = conf['place']
            link = conf['link']

            line = f'| {title} {year}| {deadline} {timezone} | {date} | {place} | {link} |'
            table.append(line)

    with open(ddl_path, 'w+') as f:
        f.write(f'# {file_title}\n\n')
        f.write('\n'.join(table))
