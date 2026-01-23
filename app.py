import sys
# Force-fix legacy urllib3 dependency
try:
    import urllib3.util
    import urllib3
    if not hasattr(urllib3, 'packages'):
        class MockPackages:
            class MockSix:
                moves = sys.modules.get('http.client')
            six = MockSix()
        urllib3.packages = MockPackages()
except ImportError:
    pass
