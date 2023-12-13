from byu_pytest_utils import max_score, with_import


def get_link_validator(LinkValidator):
    return LinkValidator(
        'https://cs111.byu.edu',
        ['/data', '/images', '/lectures']
    )


@max_score(8)
@with_import('LinkValidator', 'LinkValidator')
def test_link_validator_1(LinkValidator):
    validator = get_link_validator(LinkValidator)
    assert not validator.can_follow_link('https://byu.edu')


@max_score(8)
@with_import('LinkValidator', 'LinkValidator')
def test_link_validator_2(LinkValidator):
    validator = get_link_validator(LinkValidator)
    assert validator.can_follow_link('https://cs111.byu.edu/HW/HW01')


@max_score(8)
@with_import('LinkValidator', 'LinkValidator')
def test_link_validator_3(LinkValidator):
    validator = get_link_validator(LinkValidator)
    assert not validator.can_follow_link(
        'https://cs111.byu.edu/images/logo.png')


@max_score(8)
@with_import('LinkValidator', 'LinkValidator')
def test_link_validator_4(LinkValidator):
    validator = get_link_validator(LinkValidator)
    assert not validator.can_follow_link(
        'https://cs111.byu.edu/data/spectra1.txt')


@max_score(8)
@with_import('LinkValidator', 'LinkValidator')
def test_link_validator_5(LinkValidator):
    validator = get_link_validator(LinkValidator)
    assert validator.can_follow_link(
        'https://cs111.byu.edu/Projects/Project4/images/cat.jpg')


@max_score(10)
@with_import('webcrawler', 'parse_robots')
def test_parse_robots(parse_robots):
    assert parse_robots(
        'https://cs111.byu.edu') == ['/proj/proj4/assets/page5.html']
