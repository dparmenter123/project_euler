import time                                                
import logging

################################################################
# logging
#
# TODO: move logging configuration into a separate file
################################################################

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

################################################################
# timer
################################################################

def timeit(method):
    '''
     decorator for timing methods

     output goes to logger at the INFO level.

     http://www.andreas-jung.com/contents/a-python-decorator-for-...
     ...measuring-the-execution-time-of-methods

     '''
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        logger.info('%r (%r, %r) %2.2f sec' % (method.__name__, args, kw, te-ts))
        return result

    return timed
