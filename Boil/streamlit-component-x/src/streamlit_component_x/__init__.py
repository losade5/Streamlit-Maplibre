from pathlib import Path
from typing import Optional

import streamlit as st
import streamlit.components.v1 as components

# Tell streamlit that there is a component called streamlit_component_x,
# and that the code to display that component is in the "frontend" folder
frontend_dir = (Path(__file__).parent / "frontend").absolute()
_component_func = components.declare_component(
	"streamlit_component_x", path=str(frontend_dir)
)

# Create the python function that will be called
def streamlit_component_x(
    data: Optional[str] = None,
    key: Optional[str] = None,
):
    """
    Display the custom map component.

    Parameters:
        data (str): A JSON string to pass to the frontend. Should contain a "view" field.
        key (str, optional): Streamlit key.
    """
    component_value = _component_func(
        data=data,
        key=key,
    )
    return component_value


def main():
    st.write("## Jobs map")
    # Example JSON string with a "view" field.
    # Valid values for "view":
    #   "country"                - Shows the whole country view
    #   "country-metro"          - Shows all metros, but pans/zooms/locks to the whole country
    #   "Texas Metropolitan Area"
    #   "Oregon Metropolitan Area"
    #   "South Carolina Area"
    #   "Ohio Metropolitan Area"
    #   "South Carolina Metropolitan Area"
    #   "Wisconsin Metropolitan Area"
    #   "Alabama Area"
    #   "New York Metropolitan Area"
    #   (plus any other metro area present in the data)
    json_str = '{"view": "country-metro"}'
    value = streamlit_component_x(data=json_str)
    #json_str2 = '{"view": "Oregon Metropolitan Area"}'
    #value2 = streamlit_component_x(data=json_str2)
    st.write(value)


if __name__ == "__main__":
    main()
