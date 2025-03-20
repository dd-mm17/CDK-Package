def smiles_depict_url(smiles: str, format: str = 'svg') -> str:
    """
    Generate the URL for the depiction of a SMILES string.
    Args:
        smiles: smiles string to depict
        format: 'svg', 'pdf', 'png', etc.
    Returns:
        URL string
    """
   
    """
    Complete the params dictionary and encode it into a URL string with the urllib.parse.urlencode function
    Remember it must be a valid link to a cdkdepict URL, you can test your URL's by just navigating to the link in your browser
    Return the URL string
    """

    params = {
        'smi': smiles,
        'zoom': '1.0',
        'abbr': 'on',
        'hdisp': 'bridgehead',
        'showtitle': 'true',
        'annotate': 'none'
    }
    params_str = urllib.parse.urlencode(params)
    return f'{CDKDEPICTLINK}/{format}?{params_str}'



def display_svg(url: str) -> None:
    # post a request to the link you construct. Remember to handle the cases where the response does not work as intented
    # Look at the response content to find the SVG data.
    # Use the display function to display the SVG data
    response = requests.get(url)
    if response.status_code == 200:
        svg_data = response.text  # Extract the SVG data from the response
        display(SVG(svg_data))  # Display the SVG in the notebook
    else:
        print(f"Failed to retrieve SVG: Status code {response.status_code}")