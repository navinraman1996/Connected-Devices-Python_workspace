'''
 This module provides a simple, and incomplete, abstraction to the SenseHAT
 library. It is intended for testing and debugging purposes only.
 
 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.
'''
from random import uniform
from _ast import Param

class SenseHat():
    rotateDeg = 270
    clearFlag = False

    def __init__(self):
        self.set_rotation(self.rotateDeg)
    
    def clear(self):
        self.clearFlag = True

    def get_humidity(self):
        return self.sense.get_humidity()
        '''
        NOTE: Below is the sample value, if the sense Hat is not used
        return 48.5
        '''
    
    def get_temperature(self):
        return self.get_temperature_from_humidity()
    
    def get_temperature_from_humidity(self):
        return self.sense.get_temperature_from_humidity()
        '''
        NOTE: Below is the sample value, if the sense Hat is not used
        return 21.4
        '''
        
    def get_temperature_from_pressure(self):
        return self.get_temperature_from_humidity()
    
    def get_pressure(self):
        return self.sense.get_pressure()
        '''
        NOTE: Below is the sample value, if the sense Hat is not used
        return 31.5
        '''
        
    def set_rotation(self, rotateDeg):
        self.rotateDeg = rotateDeg
    '''
    This function is used for setting the orientation of the text to be shown
    on the Sense Hat LED, by rotating the degree of it(rotateDeg)
    
    @param rotateDeg: A value which is used for the orientation of the text
    '''
        
    def show_letter(self, val):
        print(val)
    '''
    @param val: The letter which is to be shown
    '''
        
    def show_message(self, msg):
        print(msg)
    '''
    @param val: The message which is to be shown
    '''
    