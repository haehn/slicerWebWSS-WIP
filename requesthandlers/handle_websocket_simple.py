import numpy
from __main__ import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *

from typing import Union, Optional, Awaitable

from tornado.websocket import WebSocketHandler

class SlicerSimpleWebSocketHandler(WebSocketHandler):

    def check_origin(self, origin):
        return True

    def open(self, *args: str, **kwargs: str) -> Optional[Awaitable[None]]:
        return super().open(*args, **kwargs)

    def on_close(self) -> None:
        super().on_close()

    def on_message(self, message: Union[str, bytes]) -> Optional[Awaitable[None]]:
        
        # TODO make your own protocol
        if message=='get_coil_position':
            # you can access slicer code here
            self.write_message('1.2323 3.34324 5.34324')
