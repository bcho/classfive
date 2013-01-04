#coding: utf-8

# Read timeline defination from a text & write a .json

import json

def _read(op):
    op_handler = open(op, 'r')
    result = [i.rstrip('\n') for i in op_handler.readlines()]
    op_handler.close()
    return result

def _write(result, op):
    op_handler = open(op, 'w')
    op_handler.write(json.dumps(result))
    op_handler.close()

def _slice(_range, d):
    result = []
    while(d):
        result.append(d[0:_range])
        d = d[_range:]
    return result

def _build_date(d):
    # startDate, headline, text, media, credit, caption
    asset = {
            'media': d[3],
            'credit': d[4],
            'caption': d[5],
            }
    return {
            'startDate': d[0],
            'headline': d[1],
            'text': d[2],
            'asset': asset,
            }

def _build_dates(dates):
    return dates

def _build_header(d):
    # haedline, type, startDate, text, media, credit, caption
    asset = {
            'media': d[4],
            'credit': d[5],
            'caption': d[6],
            }
    return {
            'headline': d[0],
            'type': d[1],
            'startDate': d[2],
            'text': d[3],
            'asset': asset,
            }

def _build_timeline(header, date):
    result = header
    result['date'] = date
    return {'timeline': result}

def _build(src, des):
    source = _read(src)
    header = _build_header(source[0:7])
    dates = _build_dates([_build_date(i) for i in _slice(6, source[7:])])
    _write(_build_timeline(header, dates), des)

def _main():
    _build('source.txt', 'timeline.json')

if __name__ == '__main__':
    _main()
