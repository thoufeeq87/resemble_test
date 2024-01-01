import streamlit as st
from resemble import Resemble

st. title("Testing")

Resemble.api_key('iVzdZcQ5HrRRjMIpc3bMIwtt')

# Get your default Resemble project.
project_uuid = Resemble.v2.projects.all(1, 10)['items'][0]['uuid']
st.text_area(Resemble.v2.projects.all(1, 10)['items'][0]['uuid'])
# Get your Voice uuid. In this example, we'll obtain the first.
voice_uuid = Resemble.v2.voices.all(1, 10)['items'][0]['uuid']
print(Resemble.v2.voices.all(1, 10))
# Let's create a clip!
body = 'This is a test'
response = Resemble.v2.clips.create_sync(project_uuid,
                                          voice_uuid,
                                          body,
                                          title=None,
                                          sample_rate=None,
                                          output_format=None,
                                          precision=None,
                                          include_timestamps=None,
                                          is_public=None,
                                          is_archived=None,
                                          raw=None)

clip = response['item']
print(clip['audio_src'])
