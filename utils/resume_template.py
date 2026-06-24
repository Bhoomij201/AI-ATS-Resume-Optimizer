def create_resume_html(content):

    return f"""
    <div style="
        background:white;
        color:black;
        max-width:900px;
        margin:auto;
        padding:40px;
        border-radius:10px;
        font-family:Arial, sans-serif;
        box-shadow:0 0 15px rgba(0,0,0,0.15);
    ">

    <h1 style="
        text-align:center;
        margin-bottom:5px;
        font-size:34px;
        font-weight:bold;
    ">
        PROFESSIONAL RESUME
    </h1>

    <hr style="margin-bottom:20px;">

    <div style="
        white-space:pre-wrap;
        font-size:15px;
        line-height:1.8;
    ">
        {content}
    </div>

    </div>
    """