# Twisted, the Framework of Your Internet
# Copyright (C) 2001 Matthew W. Lefkowitz
# 
# This library is free software; you can redistribute it and/or
# modify it under the terms of version 2.1 of the GNU Lesser General Public
# License as published by the Free Software Foundation.
# 
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

"""Interface documentation"""


class IProducer:
    """A producer produces data for a consumer.
    
    If this is a streaming producer, it will only be
    asked to resume producing if it has been previously asked to pause.
    Also, if this is a streaming producer, it will ask the producer to
    pause when the buffer has reached a certain size.

    In other words, a streaming producer is expected to produce (write to
    this consumer) data in the main IO thread of some process as the result
    of a read operation, whereas a non-streaming producer is expected to
    produce data each time resumeProducing() is called.
    
    If this is a non-streaming producer, resumeProducing will be called
    immediately, to start the flow of data.  Otherwise it is assumed that
    the producer starts out life unpaused.
    """
    
    def resumeProducing(self):
        """Resume producing data.
        
        This tells a producer to re-add itself to the main loop and produce
        more data for its consumer.
        """
        pass

    def pauseProducing(self):
        """Pause producing data.
        
        Tells a producer that it has produced too much data to process for
        the time being, and to stop until resumeProducing() is called.
        """
        pass

    def stopProducing(self):
        """Stop producing data.
        
        This tells a producer that its consumer has died, so it must stop
        producing data for good.
        """
        pass

