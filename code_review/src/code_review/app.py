# import streamlit as st
# import os
# from code_review.crew import run_code_review, CodeReview

# # Page Setup
# st.set_page_config(
#     page_title="AI powered Code Review Assistant",
#     page_icon="🧠",
#     layout="wide"
# )
# logo_path = "https://trigent.com/wp-content/uploads/Trigent_Axlr8_Labs.png"
# st.markdown(
#     f"""
#     <div style="text-align:center;">
#         <img src="{logo_path}" alt="Trigent Logo" style="max-width:100%;">
#     </div>
#     """,
#     unsafe_allow_html=True
# )
# # Styling
# st.markdown("""
# <style>
#     body {
#         background-color: #f4f6f9;
#         font-family: 'Inter', sans-serif;
#     }
#     .header {
#         background: linear-gradient(135deg, #4A6CF7 0%, #3658E0 100%);
#         color: white;
#         padding: 1.5rem;
#         border-radius: 12px;
#         box-shadow: 0 12px 24px rgba(70, 108, 247, 0.2);
#         text-align: center;
#         margin-bottom: 1rem;  
#         }
#     .header h1 {
#         font-size: 2.1rem; 
#         font-weight: 800;
#         margin-bottom: 0.75rem;
#         letter-spacing: -1px;
#     }
#     .header p {
#         font-size: 1rem; 
#         opacity: 0.9;
#         max-width: 800px;
#         margin: 0 auto;
#     }
#     .section-title {
#         color: #4A6CF7;
#         font-weight: 700;
#         margin-top: 2rem;
#         margin-bottom: 1rem;
#         border-bottom: 2px solid #4A6CF7;
#         padding-bottom: 0.5rem;
#     }
#     .card {
#         background: white;
#         border-radius: 12px;
#         padding: 1.5rem;
#         box-shadow: 0 8px 16px rgba(0, 0, 0, 0.06);
#         margin-bottom: 1.5rem;
#         transition: all 0.3s ease;
#     }
#     .card:hover {
#         transform: translateY(-5px);
#         box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
#     }
#     .stButton > button {
#         background-color: #4A6CF7;
#         color: white;
#         border: none;
#         border-radius: 8px;
#         padding: 12px 24px;
#         font-weight: 600;
#         transition: all 0.3s ease;
#     }
#     .stButton > button:hover {
#         background-color: #3658E0;
#         transform: scale(1.02);
#     }
# </style>
# """, unsafe_allow_html=True)

# # Header
# st.markdown("""
# <div class='header'>
#     <h1>🧠 AI Powered Code Review Assistant</h1>
#     <p>Advanced AI-powered code analysis that provides intelligent insights, debugs complex issues, and helps you write cleaner, more efficient code.</p>
# </div>
# """, unsafe_allow_html=True)
# st.markdown("<div class='section-title'>🔍 How It Works</div>", unsafe_allow_html=True)

# st.markdown("""
# <style>
# .how-it-works-row {
#     display: flex;
#     justify-content: space-between;
#     gap: 20px;
#     margin-bottom: 1.5rem;
# }
# .how-it-works-step {
#     flex: 1;
#     background: linear-gradient(135deg, #4A6CF7 0%, #3658E0 100%);
#     color: white;
#     border-radius: 12px;
#     padding: 20px;
#     text-align: center;
#     box-shadow: 0 12px 24px rgba(70, 108, 247, 0.2);
#     transition: transform 0.3s ease;
# }
# .how-it-works-step:hover {
#     transform: translateY(-5px);
# }
# .how-it-works-step h3 {
#     margin-bottom: 10px;
#     display: flex;
#     align-items: center;
#     justify-content: center;
#     gap: 10px;
# }
# .how-it-works-step p {
#     opacity: 0.9;
# }
# .advanced-features {
#     background: white;
#     border-radius: 12px;
#     padding: 20px;
#     box-shadow: 0 8px 16px rgba(0, 0, 0, 0.06);
#     margin-top: 1.5rem;
# }
# .advanced-features h3 {
#     color: #4A6CF7;
#     border-bottom: 2px solid #4A6CF7;
#     padding-bottom: 10px;
#     margin-bottom: 15px;
# }
# .advanced-features ul {
#     list-style-type: none;
#     padding: 0;
# }
# .advanced-features ul li {
#     margin-bottom: 10px;
#     padding-left: 30px;
#     position: relative;
# }
# .advanced-features ul li:before {
#     content: '✓';
#     color: #4A6CF7;
#     position: absolute;
#     left: 0;
#     top: 0;
# }
# </style>

# <div class='how-it-works-row'>
#     <div class='how-it-works-step'>
#         <h3>📝 1. Input Code</h3>
#         <p>Paste your code directly into the text area or upload a file. We support multiple programming languages including Python, JavaScript, Java, C++, and more.</p>
#     </div>
#     <div class='how-it-works-step'>
#         <h3>🤖 2. AI Analysis</h3>
#         <p>Our advanced AI agents perform a comprehensive code review, analyzing syntax, performance, best practices, and any specific instructions you provide.</p>
#     </div>
#     <div class='how-it-works-step'>
#         <h3>📊 3. Detailed Report</h3>
#         <p>Receive an intelligent, actionable report with insights, potential improvements, and code refactoring suggestions tailored to your specific code.</p>
#     </div>
# </div>

# <div class='advanced-features'>
#     <h3>🧠 Advanced Features</h3>
#     <ul>
#         <li><strong>Multi-Model Support:</strong> Choose between Azure GPT-4o and Mistral Large for your code review</li>
#         <li><strong>Custom Instructions:</strong> Provide specific review focus areas like performance optimization or security checks</li>
#         <li><strong>Comprehensive Analysis:</strong> Covers syntax, performance, best practices, and language-specific insights</li>
#         <li><strong>Easy Download:</strong> Download the full review report as a markdown file</li>
#     </ul>
# </div>
# """, unsafe_allow_html=True)

# # Code Input
# st.markdown("<div class='section-title'>🚀 Code Analysis</div>", unsafe_allow_html=True)

# input_method = st.radio("Choose Input Method:", ["Text Input", "File Upload"])

# if input_method == "Text Input":
#     code_input = st.text_area("Paste your code here", height=300, help="Supports multiple programming languages")
    
#     uploaded_file = None
#     st.session_state.uploaded_file = None

# elif input_method == "File Upload":
#     # File uploader
#     uploaded_file = st.file_uploader("Upload a file", type=["py", "js", "java", "cpp", "cs", "go", "rb", "php", "html", "css", "txt"])
    
#     # Clear the text input if a file is uploaded
#     if uploaded_file:
#         code_input = uploaded_file.getvalue().decode("utf-8")
#         # Disable text area
#         st.text_area("Code from uploaded file", value=code_input, height=300, disabled=True)
#     else:
#         code_input = ""

# # Ensure code_input is not None
# code_input = code_input if code_input else ""


# # User Query
# st.markdown("<div class='section-title'>🤔 Specific Instruction</div>", unsafe_allow_html=True)
# user_query = st.text_input("Optional: Provide specific review instructions", placeholder="E.g., 'Refactor for performance', 'Check security vulnerabilities'")

# # LLM Selection
# st.markdown("<div class='section-title'>🧠 Model Preference</div>", unsafe_allow_html=True)
# llm_provider = st.radio("Choose LLM Provider:", options=["azure", "mistral"], index=0, horizontal=True, format_func=lambda x: {
#     "azure": "Azure GPT-4o",
#     "mistral": "Mistral Large"
# }[x])

# # Review Button
# review_button = st.button("🔬 Perform Code Review", use_container_width=True)

# # Review Results
# if review_button:
#     if not code_input.strip():
#         st.warning("Please enter or upload code first.")
#     else:
#         with st.spinner("🧠 AI agents analyzing your code..."):
#             settings = {
#                 "focus_areas": ["Syntax", "Performance", "Best Practices"],
#                 "language_specific": True,
#                 "include_examples": True,
#                 "llm_provider": llm_provider
#             }
#             result = run_code_review(code_input, settings, user_query)

#         st.markdown("<div class='section-title'>📊 Review Results</div>", unsafe_allow_html=True)
#         with st.container():
#             if "file_info" in result:
#                 st.info(f"📁 File Info: {result['file_info']}")
#             if "model_info" in result:
#                 st.success(f"🧠 Model Used: {result['model_info']}")
#             if "user_query" in result:
#                 st.markdown(f"**🎯 User Query:** {result['user_query']}")

#             st.markdown("---")

#             final_output = result.get("combined_output", "[No output received]")

#             # Render output like ChatGPT, code blocks shown properly
#             inside_code_block = False
#             code_block = []
#             for line in final_output.split("\n"):
#                 if line.strip().startswith("```"):
#                     if inside_code_block:
#                         st.code("\n".join(code_block))
#                         code_block = []
#                         inside_code_block = False
#                     else:
#                         inside_code_block = True
#                 elif inside_code_block:
#                     code_block.append(line)
#                 else:
#                     st.write(line)

#             st.download_button("💾 Download Report", final_output, file_name="code_review_report.md", mime="text/markdown", use_container_width=True)


# footer_html = """
#    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
#    <div style="text-align: center;">
#        <p>
#            Copyright © 2024 | <a href="https://trigent.com/ai/" target="_blank" aria-label="Trigent Website">Trigent Software Inc.</a> All rights reserved. |
#            <a href="https://www.linkedin.com/company/trigent-software/" target="_blank" aria-label="Trigent LinkedIn"><i class="fab fa-linkedin"></i></a> |
#            <a href="https://www.twitter.com/trigentsoftware/" target="_blank" aria-label="Trigent Twitter"><i class="fab fa-twitter"></i></a> |
#            <a href="https://www.youtube.com/channel/UCNhAbLhnkeVvV6MBFUZ8hOw" target="_blank" aria-label="Trigent Youtube"><i class="fab fa-youtube"></i></a>
#        </p>
#    </div>
#    """

# footer_css = """
#    <style>
#    .footer {
#        position: fixed;
#        z-index: 1000;
#        left: 0;
#        bottom: 0;
#        width: 100%;
#        background-color: white;
#        color: black;
#        text-align: center;
#    }
#    [data-testid="stSidebarNavItems"] {
#        max-height: 100%!important;
#    }
#    [data-testid="collapsedControl"] {
#        display: none;
#    }
#    </style>
#    """

# footer = f"{footer_css}<div class='footer'>{footer_html}</div>"

# st.markdown(footer, unsafe_allow_html=True)



# import streamlit as st
# import os
# from code_review.crew import run_code_review, CodeReview

# # Page Setup
# st.set_page_config(
#     page_title="AI powered Code Review Assistant",
#     page_icon="🧠",
#     layout="wide"
# )

# logo_path = "https://trigent.com/wp-content/uploads/Trigent_Axlr8_Labs.png"
# st.markdown(
#     f"""
#     <div style="text-align:center;">
#         <img src="{logo_path}" alt="Trigent Logo" style="max-width:100%;">
#     </div>
#     """,
#     unsafe_allow_html=True
# )

# # Styling
# st.markdown("""
# <style>
#     body {
#         background-color: #f4f6f9;
#         font-family: 'Inter', sans-serif;
#     }
#     .header {
#         background: linear-gradient(135deg, #4A6CF7 0%, #3658E0 100%);
#         color: white;
#         padding: 1.5rem;
#         border-radius: 12px;
#         box-shadow: 0 12px 24px rgba(70, 108, 247, 0.2);
#         text-align: center;
#         margin-bottom: 1rem;
#     }
#     .header h1 {
#         font-size: 2.1rem;
#         font-weight: 800;
#         margin-bottom: 0.75rem;
#         letter-spacing: -1px;
#     }
#     .header p {
#         font-size: 1rem;
#         opacity: 0.9;
#         max-width: 800px;
#         margin: 0 auto;
#     }
#     .section-title {
#         color: #4A6CF7;
#         font-weight: 700;
#         margin-top: 2rem;
#         margin-bottom: 1rem;
#         border-bottom: 2px solid #4A6CF7;
#         padding-bottom: 0.5rem;
#     }
#     .card {
#         background: white;
#         border-radius: 12px;
#         padding: 1.5rem;
#         box-shadow: 0 8px 16px rgba(0, 0, 0, 0.06);
#         margin-bottom: 1.5rem;
#         transition: all 0.3s ease;
#     }
#     .card:hover {
#         transform: translateY(-5px);
#         box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
#     }
#     .stButton > button {
#         background-color: #4A6CF7;
#         color: white;
#         border: none;
#         border-radius: 8px;
#         padding: 12px 24px;
#         font-weight: 600;
#         transition: all 0.3s ease;
#     }
#     .stButton > button:hover {
#         background-color: #3658E0;
#         transform: scale(1.02);
#     }
# </style>
# """, unsafe_allow_html=True)

# # Header
# st.markdown("""
# <div class='header'>
#     <h1>🧠 AI Powered Code Review Assistant</h1>
#     <p>Advanced AI-powered code analysis that provides intelligent insights, debugs complex issues, and helps you write cleaner, more efficient code.</p>
# </div>
# """, unsafe_allow_html=True)

# st.markdown("<div class='section-title'>🚀 Code Analysis</div>", unsafe_allow_html=True)
# input_method = st.radio("Choose Input Method:", ["Text Input", "File Upload"])

# if input_method == "Text Input":
#     code_input = st.text_area("Paste your code here", height=300)
#     uploaded_file = None
#     st.session_state.uploaded_file = None
# else:
#     uploaded_file = st.file_uploader("Upload a file", type=["py", "js", "java", "cpp", "cs", "go", "rb", "php", "html", "css", "txt"])
#     if uploaded_file:
#         code_input = uploaded_file.getvalue().decode("utf-8")
#         st.text_area("Code from uploaded file", value=code_input, height=300, disabled=True)
#     else:
#         code_input = ""

# code_input = code_input if code_input else ""

# st.markdown("<div class='section-title'>🤔 Specific Instruction</div>", unsafe_allow_html=True)
# user_query = st.text_input("Optional: Provide specific review instructions")

# st.markdown("<div class='section-title'>🧠 Model Preference</div>", unsafe_allow_html=True)
# llm_provider = st.radio("Choose LLM Provider:", options=["azure", "mistral"], index=0, horizontal=True, format_func=lambda x: {
#     "azure": "Azure GPT-4o",
#     "mistral": "Mistral Large"
# }[x])

# review_button = st.button("🔬 Perform Code Review", use_container_width=True)

# if review_button:
#     if not code_input.strip():
#         st.warning("Please enter or upload code first.")
#     else:
#         with st.spinner("🧠 AI agents analyzing your code..."):
#             settings = {
#                 "focus_areas": ["Syntax", "Performance", "Best Practices"],
#                 "language_specific": True,
#                 "include_examples": True,
#                 "llm_provider": llm_provider
#             }
#             result = run_code_review(code_input, settings, user_query)

#         st.markdown("<div class='section-title'>📊 Review Results</div>", unsafe_allow_html=True)
#         with st.container():
#             if "file_info" in result:
#                 st.info(f"📁 File Info: {result['file_info']}")
#             if "model_info" in result:
#                 st.success(f"🧠 Model Used: {result['model_info']}")
#             if "user_query" in result:
#                 st.markdown(f"**🎯 User Query:** {result['user_query']}")

#             st.markdown("---")

#             final_output = result.get("combined_output", "[No output received]")

#             inside_code_block = False
#             code_block = []
#             language_hint = ""

#             for line in final_output.split("\n"):
#                 if line.strip().startswith("```"):
#                     if inside_code_block:
#                         st.code("\n".join(code_block), language=language_hint or None)
#                         code_block = []
#                         inside_code_block = False
#                         language_hint = ""
#                     else:
#                         inside_code_block = True
#                         language_hint = line.strip().lstrip("`").strip()
#                 elif inside_code_block:
#                     code_block.append(line)
#                 else:
#                     st.markdown(line)

#             st.download_button("💾 Download Report", final_output, file_name="code_review_report.md", mime="text/markdown", use_container_width=True)

# # Footer
# footer_html = """
#    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
#    <div style="text-align: center;">
#        <p>
#            Copyright © 2024 | <a href="https://trigent.com/ai/" target="_blank">Trigent Software Inc.</a> All rights reserved. |
#            <a href="https://www.linkedin.com/company/trigent-software/" target="_blank"><i class="fab fa-linkedin"></i></a> |
#            <a href="https://www.twitter.com/trigentsoftware/" target="_blank"><i class="fab fa-twitter"></i></a> |
#            <a href="https://www.youtube.com/channel/UCNhAbLhnkeVvV6MBFUZ8hOw" target="_blank"><i class="fab fa-youtube"></i></a>
#        </p>
#    </div>
# """

# footer_css = """
#    <style>
#    .footer {
#        position: fixed;
#        z-index: 1000;
#        left: 0;
#        bottom: 0;
#        width: 100%;
#        background-color: white;
#        color: black;
#        text-align: center;
#    }
#    [data-testid="stSidebarNavItems"] {
#        max-height: 100%!important;
#    }
#    [data-testid="collapsedControl"] {
#        display: none;
#    }
#    </style>
# """

# footer = f"{footer_css}<div class='footer'>{footer_html}</div>"

# st.markdown(footer, unsafe_allow_html=True)


# import streamlit as st
# import os
# from code_review.crew import run_code_review, CodeReview

# # Page Setup
# st.set_page_config(
#     page_title="AI powered Code Review Assistant",
#     page_icon="🧠",
#     layout="wide"
# )

# logo_path = "https://trigent.com/wp-content/uploads/Trigent_Axlr8_Labs.png"
# st.markdown(
#     f"""
#     <div style="text-align:center;">
#         <img src="{logo_path}" alt="Trigent Logo" style="max-width:100%;">
#     </div>
#     """,
#     unsafe_allow_html=True
# )

# # Styling
# st.markdown("""
# <style>
#     body {
#         background-color: #f4f6f9;
#         font-family: 'Inter', sans-serif;
#     }
#     .header {
#         background: linear-gradient(135deg, #4A6CF7 0%, #3658E0 100%);
#         color: white;
#         padding: 1.5rem;
#         border-radius: 12px;
#         box-shadow: 0 12px 24px rgba(70, 108, 247, 0.2);
#         text-align: center;
#         margin-bottom: 1rem;
#     }
#     .header h1 {
#         font-size: 2.1rem;
#         font-weight: 800;
#         margin-bottom: 0.75rem;
#         letter-spacing: -1px;
#     }
#     .header p {
#         font-size: 1rem;
#         opacity: 0.9;
#         max-width: 800px;
#         margin: 0 auto;
#     }
#     .section-title {
#         color: #4A6CF7;
#         font-weight: 700;
#         margin-top: 2rem;
#         margin-bottom: 1rem;
#         border-bottom: 2px solid #4A6CF7;
#         padding-bottom: 0.5rem;
#     }
#     .card {
#         background: white;
#         border-radius: 12px;
#         padding: 1.5rem;
#         box-shadow: 0 8px 16px rgba(0, 0, 0, 0.06);
#         margin-bottom: 1.5rem;
#         transition: all 0.3s ease;
#     }
#     .card:hover {
#         transform: translateY(-5px);
#         box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
#     }
#     .stButton > button {
#         background-color: #4A6CF7;
#         color: white;
#         border: none;
#         border-radius: 8px;
#         padding: 12px 24px;
#         font-weight: 600;
#         transition: all 0.3s ease;
#     }
#     .stButton > button:hover {
#         background-color: #3658E0;
#         transform: scale(1.02);
#     }
# </style>
# """, unsafe_allow_html=True)

# # Header
# st.markdown("""
# <div class='header'>
#     <h1>🧠 AI Powered Code Review Assistant</h1>
#     <p>Advanced AI-powered code analysis that provides intelligent insights, debugs complex issues, and helps you write cleaner, more efficient code.</p>
# </div>
# """, unsafe_allow_html=True)

# st.markdown("<div class='section-title'>🚀 Code Analysis</div>", unsafe_allow_html=True)
# input_method = st.radio("Choose Input Method:", ["Text Input", "File Upload"])

# # Initialize session state for storing uploaded files
# if 'uploaded_files' not in st.session_state:
#     st.session_state.uploaded_files = {}

# if 'combined_code' not in st.session_state:
#     st.session_state.combined_code = ""

# if 'current_file' not in st.session_state:
#     st.session_state.current_file = None

# if input_method == "Text Input":
#     code_input = st.text_area("Paste your code here", height=300)
#     st.session_state.uploaded_files = {}
    
# else:  # File Upload
#     # Multi-file uploader
#     uploaded_files = st.file_uploader(
#         "Upload code file(s)", 
#         type=["py", "js", "java", "cpp", "cs", "go", "rb", "php", "html", "css", "txt", "md", "json", "xml", "yaml", "yml"],
#         accept_multiple_files=True
#     )
    
#     # Process uploaded files
#     if uploaded_files:
#         for uploaded_file in uploaded_files:
#             try:
#                 file_content = uploaded_file.getvalue().decode("utf-8")
#                 # Store in session state with filename as key
#                 st.session_state.uploaded_files[uploaded_file.name] = file_content
#             except Exception as e:
#                 st.error(f"Error processing file {uploaded_file.name}: {str(e)}")
    
#     # File selection if there are multiple files
#     if len(st.session_state.uploaded_files) > 0:
#         file_options = list(st.session_state.uploaded_files.keys())
        
#         # Add option for all files
#         if len(file_options) > 1:
#             file_options.insert(0, "All Files (Combined)")
        
#         selected_file = st.selectbox(
#             "Select file to review:", 
#             file_options,
#             index=0
#         )
        
#         st.session_state.current_file = selected_file
        
#         # Prepare code based on selection
#         if selected_file == "All Files (Combined)":
#             # Combine all files with headers
#             combined_text = ""
#             for filename, content in st.session_state.uploaded_files.items():
#                 combined_text += f"# File: {filename}\n{content}\n\n"
#             code_input = combined_text
#             st.session_state.combined_code = combined_text
#             st.text_area("Combined code preview", value=combined_text, height=300, disabled=True)
#         else:
#             # Show single file
#             code_input = st.session_state.uploaded_files[selected_file]
#             st.text_area("Code from uploaded file", value=code_input, height=300, disabled=True)
            
#         # Option to clear uploaded files
#         if st.button("Clear Uploaded Files"):
#             st.session_state.uploaded_files = {}
#             st.session_state.combined_code = ""
#             st.session_state.current_file = None
#             st.rerun()
#     else:
#         st.info("Please upload one or more code files.")
#         code_input = ""

# # Ensure code_input is not None
# code_input = code_input if code_input else ""

# st.markdown("<div class='section-title'>🤔 Specific Instruction</div>", unsafe_allow_html=True)
# user_query = st.text_input("Optional: Provide specific review instructions", 
#                           placeholder="E.g., 'Refactor for performance', 'Check security vulnerabilities'")

# st.markdown("<div class='section-title'>🧠 Model Preference</div>", unsafe_allow_html=True)
# llm_provider = st.radio("Choose LLM Provider:", options=["azure", "mistral"], index=0, horizontal=True, format_func=lambda x: {
#     "azure": "Azure GPT-4o",
#     "mistral": "Mistral Large"
# }[x])

# review_button = st.button("🔬 Perform Code Review", use_container_width=True)

# if review_button:
#     if not code_input.strip():
#         st.warning("Please enter or upload code first.")
#     else:
#         with st.spinner("🧠 AI agents analyzing your code..."):
#             settings = {
#                 "focus_areas": ["Syntax", "Performance", "Best Practices"],
#                 "language_specific": True,
#                 "include_examples": True,
#                 "llm_provider": llm_provider
#             }
            
#             # Add file info to user query if multiple files are being analyzed
#             enhanced_query = user_query
#             if input_method == "File Upload" and st.session_state.current_file == "All Files (Combined)":
#                 file_list = ", ".join(st.session_state.uploaded_files.keys())
#                 enhanced_query = f"{user_query}\n[Multiple files being analyzed: {file_list}]"
            
#             result = run_code_review(code_input, settings, enhanced_query)

#         st.markdown("<div class='section-title'>📊 Review Results</div>", unsafe_allow_html=True)
#         with st.container():
#             if "file_info" in result:
#                 file_info = result['file_info']
#                 if st.session_state.current_file == "All Files (Combined)":
#                     file_info = f"Multiple files: {', '.join(st.session_state.uploaded_files.keys())}"
#                 st.info(f"📁 File Info: {file_info}")
#             if "model_info" in result:
#                 st.success(f"🧠 Model Used: {result['model_info']}")
#             if "user_query" in result:
#                 st.markdown(f"**🎯 User Query:** {result['user_query']}")

#             st.markdown("---")

#             final_output = result.get("combined_output", "[No output received]")

#             inside_code_block = False
#             code_block = []
#             language_hint = ""

#             for line in final_output.split("\n"):
#                 if line.strip().startswith("```"):
#                     if inside_code_block:
#                         st.code("\n".join(code_block), language=language_hint or None)
#                         code_block = []
#                         inside_code_block = False
#                         language_hint = ""
#                     else:
#                         inside_code_block = True
#                         language_hint = line.strip().lstrip("`").strip()
#                 elif inside_code_block:
#                     code_block.append(line)
#                 else:
#                     st.markdown(line)

#             st.download_button("💾 Download Report", final_output, file_name="code_review_report.md", mime="text/markdown", use_container_width=True)


# import streamlit as st
# import os
# from code_review.crew import run_code_review, CodeReview,generate_test_cases

# # Page Setup
# st.set_page_config(
#     page_title="AI powered Code Review Assistant",
#     page_icon="🧠",
#     layout="wide"
# )

# logo_path = "https://trigent.com/wp-content/uploads/Trigent_Axlr8_Labs.png"
# st.markdown(
#     f"""
#     <div style="text-align:center;">
#         <img src="{logo_path}" alt="Trigent Logo" style="max-width:100%;">
#     </div>
#     """,
#     unsafe_allow_html=True
# )

# # Styling
# st.markdown("""
# <style>
#     body {
#         background-color: #f4f6f9;
#         font-family: 'Inter', sans-serif;
#     }
#     .header {
#         background: linear-gradient(135deg, #4A6CF7 0%, #3658E0 100%);
#         color: white;
#         padding: 1.5rem;
#         border-radius: 12px;
#         box-shadow: 0 12px 24px rgba(70, 108, 247, 0.2);
#         text-align: center;
#         margin-bottom: 1rem;
#     }
#     .header h1 {
#         font-size: 2.1rem;
#         font-weight: 800;
#         margin-bottom: 0.75rem;
#         letter-spacing: -1px;
#     }
#     .header p {
#         font-size: 1rem;
#         opacity: 0.9;
#         max-width: 800px;
#         margin: 0 auto;
#     }
#     .section-title {
#         color: #4A6CF7;
#         font-weight: 700;
#         margin-top: 2rem;
#         margin-bottom: 1rem;
#         border-bottom: 2px solid #4A6CF7;
#         padding-bottom: 0.5rem;
#     }
#     .card {
#         background: white;
#         border-radius: 12px;
#         padding: 1.5rem;
#         box-shadow: 0 8px 16px rgba(0, 0, 0, 0.06);
#         margin-bottom: 1.5rem;
#         transition: all 0.3s ease;
#     }
#     .card:hover {
#         transform: translateY(-5px);
#         box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
#     }
#     .stButton > button {
#         background-color: #4A6CF7;
#         color: white;
#         border: none;
#         border-radius: 8px;
#         padding: 12px 24px;
#         font-weight: 600;
#         transition: all 0.3s ease;
#     }
#     .stButton > button:hover {
#         background-color: #3658E0;
#         transform: scale(1.02);
#     }
# </style>
# """, unsafe_allow_html=True)

# # Header
# st.markdown("""
# <div class='header'>
#     <h1>🧠 AI Powered Code Review Assistant</h1>
#     <p>Advanced AI-powered code analysis that provides intelligent insights, debugs complex issues, and helps you write cleaner, more efficient code.</p>
# </div>
# """, unsafe_allow_html=True)

# st.markdown("<div class='section-title'>🚀 Code Analysis</div>", unsafe_allow_html=True)
# input_method = st.radio("Choose Input Method:", ["Text Input", "File Upload"])

# if 'uploaded_files' not in st.session_state:
#     st.session_state.uploaded_files = {}
# if 'combined_code' not in st.session_state:
#     st.session_state.combined_code = ""
# if 'current_file' not in st.session_state:
#     st.session_state.current_file = None

# if 'test_cases_generated' not in st.session_state:
#     st.session_state.test_cases_generated = False
# if 'test_cases' not in st.session_state:
#     st.session_state.test_cases = ""
# beginner_mode = st.toggle("🧒 Beginner Mode (Explain like I'm 5)")

# if input_method == "Text Input":
#     code_input = st.text_area("Paste your code here", height=300)
#     st.session_state.uploaded_files = {}
# else:
#     uploaded_files = st.file_uploader(
#         "Upload code file(s)", 
#         type=["py", "js", "java", "cpp", "cs", "go", "rb", "php", "html", "css", "txt", "md", "json", "xml", "yaml", "yml"],
#         accept_multiple_files=True
#     )
#     if uploaded_files:
#         for uploaded_file in uploaded_files:
#             try:
#                 file_content = uploaded_file.getvalue().decode("utf-8")
#                 st.session_state.uploaded_files[uploaded_file.name] = file_content
#             except Exception as e:
#                 st.error(f"Error processing file {uploaded_file.name}: {str(e)}")
#     if len(st.session_state.uploaded_files) > 0:
#         file_options = list(st.session_state.uploaded_files.keys())
#         if len(file_options) > 1:
#             file_options.insert(0, "All Files (Combined)")
#         selected_file = st.selectbox("Select file to review:", file_options, index=0)
#         st.session_state.current_file = selected_file
#         if selected_file == "All Files (Combined)":
#             combined_text = ""
#             for filename, content in st.session_state.uploaded_files.items():
#                 combined_text += f"# File: {filename}\n{content}\n\n"
#             code_input = combined_text
#             st.session_state.combined_code = combined_text
#             st.text_area("Combined code preview", value=combined_text, height=300, disabled=True)
#         else:
#             code_input = st.session_state.uploaded_files[selected_file]
#             st.text_area("Code from uploaded file", value=code_input, height=300, disabled=True)
#         if st.button("Clear Uploaded Files"):
#             st.session_state.uploaded_files = {}
#             st.session_state.combined_code = ""
#             st.session_state.current_file = None
#             st.rerun()
#     else:
#         st.info("Please upload one or more code files.")
#         code_input = ""

# code_input = code_input if code_input else ""

# st.markdown("<div class='section-title'>🤔 Specific Instruction</div>", unsafe_allow_html=True)
# user_query = st.text_input("Optional: Provide specific review instructions", 
#                           placeholder="E.g., 'Refactor for performance', 'Check security vulnerabilities'")

# st.markdown("<div class='section-title'>🧠 Model Preference</div>", unsafe_allow_html=True)
# llm_provider = st.radio("Choose LLM Provider:", options=["azure", "mistral"], index=0, horizontal=True, format_func=lambda x: {
#     "azure": "Azure GPT-4o",
#     "mistral": "Mistral Large"
# }[x])

# review_button = st.button("🔬 Perform Code Review", use_container_width=True)

# if review_button:
#     if not code_input.strip():
#         st.warning("Please enter or upload code first.")
#     else:
#         with st.spinner("🧠 AI agents analyzing your code..."):
#             settings = {
#                 "focus_areas": ["Syntax", "Performance", "Best Practices"],
#                 "language_specific": True,
#                 "include_examples": True,
#                 "llm_provider": llm_provider,
#                 "beginner_mode": beginner_mode
#             }
#             enhanced_query = user_query
#             if beginner_mode:
#                 enhanced_query = (user_query + "\nPlease explain the code in beginner-friendly terms." if user_query else "Explain this code in beginner-friendly terms.")
#             if input_method == "File Upload" and st.session_state.current_file == "All Files (Combined)":
#                 file_list = ", ".join(st.session_state.uploaded_files.keys())
#                 enhanced_query += f"\n[Multiple files being analyzed: {file_list}]"
#             result = run_code_review(code_input, settings, enhanced_query)

#         st.markdown("<div class='section-title'>📊 Review Results</div>", unsafe_allow_html=True)
#         with st.container():
#             if "file_info" in result:
#                 file_info = result['file_info']
#                 if st.session_state.current_file == "All Files (Combined)":
#                     file_info = f"Multiple files: {', '.join(st.session_state.uploaded_files.keys())}"
#                 st.info(f"📁 File Info: {file_info}")
#             if "model_info" in result:
#                 st.success(f"🧠 Model Used: {result['model_info']}")
#             if "user_query" in result:
#                 st.markdown(f"**🎯 User Query:** {result['user_query']}")

#             st.markdown("---")

#             final_output = result.get("combined_output", "[No output received]")
#             inside_code_block = False
#             code_block = []
#             language_hint = ""

#             for line in final_output.split("\n"):
#                 if line.strip().startswith("```"):
#                     if inside_code_block:
#                         st.code("\n".join(code_block), language=language_hint or None)
#                         code_block = []
#                         inside_code_block = False
#                         language_hint = ""
#                     else:
#                         inside_code_block = True
#                         language_hint = line.strip().lstrip("`").strip()
#                 elif inside_code_block:
#                     code_block.append(line)
#                 else:
#                     st.markdown(line)

#             st.download_button("💾 Download Report", final_output, file_name="code_review_report.md", mime="text/markdown", use_container_width=True)

            
#             # Add test case generator button if user has provided a query
#             if user_query.strip():
#                 if st.button("🧪 Generate Test Cases", use_container_width=True):
#                     with st.spinner("Generating test cases..."):
#                         test_cases = generate_test_cases(code_input, user_query, llm_provider)
#                     st.markdown("<div class='section-title'>🧪 Generated Test Cases</div>", unsafe_allow_html=True)
                    
#                     # Display the test cases
#                     inside_code_block = False
#                     code_block = []
#                     language_hint = ""
                    
#                     for line in test_cases.split("\n"):
#                         if line.strip().startswith("```"):
#                             if inside_code_block:
#                                 st.code("\n".join(code_block), language=language_hint or None)
#                                 code_block = []
#                                 inside_code_block = False
#                                 language_hint = ""
#                             else:
#                                 inside_code_block = True
#                                 language_hint = line.strip().lstrip("`").strip()
#                         elif inside_code_block:
#                             code_block.append(line)
#                         else:
#                             st.markdown(line)
                    
#                     st.download_button("💾 Download Test Cases", test_cases, file_name="test_cases.md", mime="text/markdown", use_container_width=True)
# # Footer
# footer_html = """
#    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
#    <div style="text-align: center;">
#        <p>
#            Copyright © 2024 | <a href="https://trigent.com/ai/" target="_blank">Trigent Software Inc.</a> All rights reserved. |
#            <a href="https://www.linkedin.com/company/trigent-software/" target="_blank"><i class="fab fa-linkedin"></i></a> |
#            <a href="https://www.twitter.com/trigentsoftware/" target="_blank"><i class="fab fa-twitter"></i></a> |
#            <a href="https://www.youtube.com/channel/UCNhAbLhnkeVvV6MBFUZ8hOw" target="_blank"><i class="fab fa-youtube"></i></a>
#        </p>
#    </div>
# """

# footer_css = """
#    <style>
#    .footer {
#        position: fixed;
#        z-index: 1000;
#        left: 0;
#        bottom: 0;
#        width: 100%;
#        background-color: white;
#        color: black;
#        text-align: center;
#    }
#    [data-testid="stSidebarNavItems"] {
#        max-height: 100%!important;
#    }
#    [data-testid="collapsedControl"] {
#        display: none;
#    }
#    </style>
# """

# footer = f"{footer_css}<div class='footer'>{footer_html}</div>"

# st.markdown(footer, unsafe_allow_html=True)

# # Footer
# footer_html = """
#    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
#    <div style="text-align: center;">
#        <p>
#            Copyright © 2024 | <a href="https://trigent.com/ai/" target="_blank">Trigent Software Inc.</a> All rights reserved. |
#            <a href="https://www.linkedin.com/company/trigent-software/" target="_blank"><i class="fab fa-linkedin"></i></a> |
#            <a href="https://www.twitter.com/trigentsoftware/" target="_blank"><i class="fab fa-twitter"></i></a> |
#            <a href="https://www.youtube.com/channel/UCNhAbLhnkeVvV6MBFUZ8hOw" target="_blank"><i class="fab fa-youtube"></i></a>
#        </p>
#    </div>
# """

# footer_css = """
#    <style>
#    .footer {
#        position: fixed;
#        z-index: 1000;
#        left: 0;
#        bottom: 0;
#        width: 100%;
#        background-color: white;
#        color: black;
#        text-align: center;
#    }
#    [data-testid="stSidebarNavItems"] {
#        max-height: 100%!important;
#    }
#    [data-testid="collapsedControl"] {
#        display: none;
#    }
#    </style>
# """

# footer = f"{footer_css}<div class='footer'>{footer_html}</div>"

# st.markdown(footer, unsafe_allow_html=True)


# import streamlit as st
# import os
# from code_review.crew import run_code_review, CodeReview, generate_test_cases

# # Page Setup
# st.set_page_config(
#     page_title="AI powered Code Review Assistant",
#     page_icon="🧠",
#     layout="wide"
# )

# logo_path = "https://trigent.com/wp-content/uploads/Trigent_Axlr8_Labs.png"
# st.markdown(
#     f"""
#     <div style="text-align:center;">
#         <img src="{logo_path}" alt="Trigent Logo" style="max-width:100%;">
#     </div>
#     """,
#     unsafe_allow_html=True
# )

# # Styling
# st.markdown("""
# <style>
#     body {
#         background-color: #f4f6f9;
#         font-family: 'Inter', sans-serif;
#     }
#     .header {
#         background: linear-gradient(135deg, #4A6CF7 0%, #3658E0 100%);
#         color: white;
#         padding: 1.5rem;
#         border-radius: 12px;
#         box-shadow: 0 12px 24px rgba(70, 108, 247, 0.2);
#         text-align: center;
#         margin-bottom: 1rem;
#     }
#     .header h1 {
#         font-size: 2.1rem;
#         font-weight: 800;
#         margin-bottom: 0.75rem;
#         letter-spacing: -1px;
#     }
#     .header p {
#         font-size: 1rem;
#         opacity: 0.9;
#         max-width: 800px;
#         margin: 0 auto;
#     }
#     .section-title {
#         color: #4A6CF7;
#         font-weight: 700;
#         margin-top: 2rem;
#         margin-bottom: 1rem;
#         border-bottom: 2px solid #4A6CF7;
#         padding-bottom: 0.5rem;
#     }
#     .card {
#         background: white;
#         border-radius: 12px;
#         padding: 1.5rem;
#         box-shadow: 0 8px 16px rgba(0, 0, 0, 0.06);
#         margin-bottom: 1.5rem;
#         transition: all 0.3s ease;
#     }
#     .card:hover {
#         transform: translateY(-5px);
#         box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
#     }
#     .stButton > button {
#         background-color: #4A6CF7;
#         color: white;
#         border: none;
#         border-radius: 8px;
#         padding: 12px 24px;
#         font-weight: 600;
#         transition: all 0.3s ease;
#     }
#     .stButton > button:hover {
#         background-color: #3658E0;
#         transform: scale(1.02);
#     }
# </style>
# """, unsafe_allow_html=True)

# # Header
# st.markdown("""
# <div class='header'>
#     <h1>🧠 AI Powered Code Review Assistant</h1>
#     <p>Advanced AI-powered code analysis that provides intelligent insights, debugs complex issues, and helps you write cleaner, more efficient code.</p>
# </div>
# """, unsafe_allow_html=True)

# # Initialize session state variables
# if 'uploaded_files' not in st.session_state:
#     st.session_state.uploaded_files = {}
# if 'combined_code' not in st.session_state:
#     st.session_state.combined_code = ""
# if 'current_file' not in st.session_state:
#     st.session_state.current_file = None
# if 'test_cases_generated' not in st.session_state:
#     st.session_state.test_cases_generated = False
# if 'test_cases' not in st.session_state:
#     st.session_state.test_cases = ""
# if 'review_completed' not in st.session_state:
#     st.session_state.review_completed = False
# if 'review_results' not in st.session_state:
#     st.session_state.review_results = None

# st.markdown("<div class='section-title'>🚀 Code Analysis</div>", unsafe_allow_html=True)
# input_method = st.radio("Choose Input Method:", ["Text Input", "File Upload"])

# beginner_mode = st.toggle("🧒 Beginner Mode (Explain like I'm 5)")

# if input_method == "Text Input":
#     code_input = st.text_area("Paste your code here", height=300)
#     st.session_state.uploaded_files = {}
# else:
#     uploaded_files = st.file_uploader(
#         "Upload code file(s)", 
#         type=["py", "js", "java", "cpp", "cs", "go", "rb", "php", "html", "css", "txt", "md", "json", "xml", "yaml", "yml"],
#         accept_multiple_files=True
#     )
#     if uploaded_files:
#         for uploaded_file in uploaded_files:
#             try:
#                 file_content = uploaded_file.getvalue().decode("utf-8")
#                 st.session_state.uploaded_files[uploaded_file.name] = file_content
#             except Exception as e:
#                 st.error(f"Error processing file {uploaded_file.name}: {str(e)}")
#     if len(st.session_state.uploaded_files) > 0:
#         file_options = list(st.session_state.uploaded_files.keys())
#         if len(file_options) > 1:
#             file_options.insert(0, "All Files (Combined)")
#         selected_file = st.selectbox("Select file to review:", file_options, index=0)
#         st.session_state.current_file = selected_file
#         if selected_file == "All Files (Combined)":
#             combined_text = ""
#             for filename, content in st.session_state.uploaded_files.items():
#                 combined_text += f"# File: {filename}\n{content}\n\n"
#             code_input = combined_text
#             st.session_state.combined_code = combined_text
#             st.text_area("Combined code preview", value=combined_text, height=300, disabled=True)
#         else:
#             code_input = st.session_state.uploaded_files[selected_file]
#             st.text_area("Code from uploaded file", value=code_input, height=300, disabled=True)
#         if st.button("Clear Uploaded Files"):
#             st.session_state.uploaded_files = {}
#             st.session_state.combined_code = ""
#             st.session_state.current_file = None
#             st.rerun()
#     else:
#         st.info("Please upload one or more code files.")
#         code_input = ""

# code_input = code_input if code_input else ""

# st.markdown("<div class='section-title'>🤔 Specific Instruction</div>", unsafe_allow_html=True)
# user_query = st.text_input("Optional: Provide specific review instructions", 
#                           placeholder="E.g., 'Refactor for performance', 'Check security vulnerabilities'")

# st.markdown("<div class='section-title'>🧠 Model Preference</div>", unsafe_allow_html=True)
# llm_provider = st.radio("Choose LLM Provider:", options=["azure", "mistral"], index=0, horizontal=True, format_func=lambda x: {
#     "azure": "Azure GPT-4o",
#     "mistral": "Mistral Large"
# }[x])

# # Function to run code review
# def perform_code_review():
#     if not code_input.strip():
#         st.warning("Please enter or upload code first.")
#         return False
    
#     with st.spinner("🧠 AI agents analyzing your code..."):
#         settings = {
#             "focus_areas": ["Syntax", "Performance", "Best Practices"],
#             "language_specific": True,
#             "include_examples": True,
#             "llm_provider": llm_provider,
#             "beginner_mode": beginner_mode
#         }
#         enhanced_query = user_query
#         if beginner_mode:
#             enhanced_query = (user_query + "\nPlease explain the code in beginner-friendly terms." if user_query else "Explain this code in beginner-friendly terms.")
#         if input_method == "File Upload" and st.session_state.current_file == "All Files (Combined)":
#             file_list = ", ".join(st.session_state.uploaded_files.keys())
#             enhanced_query += f"\n[Multiple files being analyzed: {file_list}]"
#         result = run_code_review(code_input, settings, enhanced_query)
#         st.session_state.review_results = result
#         st.session_state.review_completed = True
#     return True

# # Function to generate test cases
# def create_test_cases():
#     with st.spinner("Generating test cases..."):
#         test_cases = generate_test_cases(code_input, user_query, llm_provider)
#         st.session_state.test_cases = test_cases
#         st.session_state.test_cases_generated = True

# # Main action buttons
# col1, col2 = st.columns(2)
# with col1:
#     review_button = st.button("🔬 Perform Code Review", use_container_width=True)
# with col2:
#     if user_query.strip():
#         test_button = st.button("🧪 Generate Test Cases", use_container_width=True, disabled=not code_input.strip())

# # Handle button clicks
# if review_button:
#     perform_code_review()

# if 'test_button' in locals() and test_button:
#     create_test_cases()

# # Display review results if available
# if st.session_state.review_completed and st.session_state.review_results:
#     st.markdown("<div class='section-title'>📊 Review Results</div>", unsafe_allow_html=True)
#     with st.container():
#         result = st.session_state.review_results
#         if "file_info" in result:
#             file_info = result['file_info']
#             if st.session_state.current_file == "All Files (Combined)":
#                 file_info = f"Multiple files: {', '.join(st.session_state.uploaded_files.keys())}"
#             st.info(f"📁 File Info: {file_info}")
#         if "model_info" in result:
#             st.success(f"🧠 Model Used: {result['model_info']}")
#         if "user_query" in result:
#             st.markdown(f"**🎯 User Query:** {result['user_query']}")

#         st.markdown("---")

#         final_output = result.get("combined_output", "[No output received]")
#         inside_code_block = False
#         code_block = []
#         language_hint = ""

#         for line in final_output.split("\n"):
#             if line.strip().startswith("```"):
#                 if inside_code_block:
#                     st.code("\n".join(code_block), language=language_hint or None)
#                     code_block = []
#                     inside_code_block = False
#                     language_hint = ""
#                 else:
#                     inside_code_block = True
#                     language_hint = line.strip().lstrip("`").strip()
#             elif inside_code_block:
#                 code_block.append(line)
#             else:
#                 st.markdown(line)

#         st.download_button("💾 Download Report", final_output, file_name="code_review_report.md", mime="text/markdown", use_container_width=True)

# # Display test cases if generated
# if st.session_state.test_cases_generated:
#     st.markdown("<div class='section-title'>🧪 Generated Test Cases</div>", unsafe_allow_html=True)
    
#     # Display the test cases
#     inside_code_block = False
#     code_block = []
#     language_hint = ""
    
#     for line in st.session_state.test_cases.split("\n"):
#         if line.strip().startswith("```"):
#             if inside_code_block:
#                 st.code("\n".join(code_block), language=language_hint or None)
#                 code_block = []
#                 inside_code_block = False
#                 language_hint = ""
#             else:
#                 inside_code_block = True
#                 language_hint = line.strip().lstrip("`").strip()
#         elif inside_code_block:
#             code_block.append(line)
#         else:
#             st.markdown(line)
    
#     st.download_button("💾 Download Test Cases", st.session_state.test_cases, file_name="test_cases.md", mime="text/markdown", use_container_width=True)

# # Footer (keeping only one instance)
# footer_html = """
#    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
#    <div style="text-align: center;">
#        <p>
#            Copyright © 2024 | <a href="https://trigent.com/ai/" target="_blank">Trigent Software Inc.</a> All rights reserved. |
#            <a href="https://www.linkedin.com/company/trigent-software/" target="_blank"><i class="fab fa-linkedin"></i></a> |
#            <a href="https://www.twitter.com/trigentsoftware/" target="_blank"><i class="fab fa-twitter"></i></a> |
#            <a href="https://www.youtube.com/channel/UCNhAbLhnkeVvV6MBFUZ8hOw" target="_blank"><i class="fab fa-youtube"></i></a>
#        </p>
#    </div>
# """

# footer_css = """
#    <style>
#    .footer {
#        position: fixed;
#        z-index: 1000;
#        left: 0;
#        bottom: 0;
#        width: 100%;
#        background-color: white;
#        color: black;
#        text-align: center;
#    }
#    [data-testid="stSidebarNavItems"] {
#        max-height: 100%!important;
#    }
#    [data-testid="collapsedControl"] {
#        display: none;
#    }
#    </style>
# """

# footer = f"{footer_css}<div class='footer'>{footer_html}</div>"

# st.markdown(footer, unsafe_allow_html=True)


# import streamlit as st
# import os
# from code_review.crew import run_code_review, CodeReview, generate_test_cases

# # Page Setup
# st.set_page_config(
#     page_title="AI powered Code Review Assistant",
#     page_icon="🧠",
#     layout="wide"
# )

# logo_path = "https://trigent.com/wp-content/uploads/Trigent_Axlr8_Labs.png"
# st.markdown(
#     f"""
#     <div style="text-align:center;">
#         <img src="{logo_path}" alt="Trigent Logo" style="max-width:100%;">
#     </div>
#     """,
#     unsafe_allow_html=True
# )

# # Styling
# st.markdown("""
# <style>
#     body {
#         background-color: #f4f6f9;
#         font-family: 'Inter', sans-serif;
#     }
#     .header {
#         background: linear-gradient(135deg, #4A6CF7 0%, #3658E0 100%);
#         color: white;
#         padding: 1.5rem;
#         border-radius: 12px;
#         box-shadow: 0 12px 24px rgba(70, 108, 247, 0.2);
#         text-align: center;
#         margin-bottom: 1rem;
#     }
#     .header h1 {
#         font-size: 2.1rem;
#         font-weight: 800;
#         margin-bottom: 0.75rem;
#         letter-spacing: -1px;
#     }
#     .header p {
#         font-size: 1rem;
#         opacity: 0.9;
#         max-width: 800px;
#         margin: 0 auto;
#     }
#     .section-title {
#         color: #4A6CF7;
#         font-weight: 700;
#         margin-top: 2rem;
#         margin-bottom: 1rem;
#         border-bottom: 2px solid #4A6CF7;
#         padding-bottom: 0.5rem;
#     }
#     .card {
#         background: white;
#         border-radius: 12px;
#         padding: 1.5rem;
#         box-shadow: 0 8px 16px rgba(0, 0, 0, 0.06);
#         margin-bottom: 1.5rem;
#         transition: all 0.3s ease;
#     }
#     .card:hover {
#         transform: translateY(-5px);
#         box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
#     }
#     .stButton > button {
#         background-color: #4A6CF7;
#         color: white;
#         border: none;
#         border-radius: 8px;
#         padding: 12px 24px;
#         font-weight: 600;
#         transition: all 0.3s ease;
#     }
#     .stButton > button:hover {
#         background-color: #3658E0;
#         transform: scale(1.02);
#     }
# </style>
# """, unsafe_allow_html=True)

# # Header
# st.markdown("""
# <div class='header'>
#     <h1>🧠 AI Powered Code Review Assistant</h1>
#     <p>Advanced AI-powered code analysis that provides intelligent insights, debugs complex issues, and helps you write cleaner, more efficient code.</p>
# </div>
# """, unsafe_allow_html=True)

# st.markdown("<div class='section-title'>🔍 How It Works</div>", unsafe_allow_html=True)

# st.markdown("""
# <style>
# .how-it-works-row {
#     display: flex;
#     justify-content: space-between;
#     gap: 20px;
#     margin-bottom: 1.5rem;
# }
# .how-it-works-step {
#     flex: 1;
#     background: linear-gradient(135deg, #4A6CF7 0%, #3658E0 100%);
#     color: white;
#     border-radius: 12px;
#     padding: 20px;
#     text-align: center;
#     box-shadow: 0 12px 24px rgba(70, 108, 247, 0.2);
#     transition: transform 0.3s ease;
# }
# .how-it-works-step:hover {
#     transform: translateY(-5px);
# }
# .how-it-works-step h3 {
#     margin-bottom: 10px;
#     display: flex;
#     align-items: center;
#     justify-content: center;
#     gap: 10px;
# }
# .how-it-works-step p {
#     opacity: 0.9;
# }
# .advanced-features {
#     background: white;
#     border-radius: 12px;
#     padding: 20px;
#     box-shadow: 0 8px 16px rgba(0, 0, 0, 0.06);
#     margin-top: 1.5rem;
# }
# .advanced-features h3 {
#     color: #4A6CF7;
#     border-bottom: 2px solid #4A6CF7;
#     padding-bottom: 10px;
#     margin-bottom: 15px;
# }
# .advanced-features ul {
#     list-style-type: none;
#     padding: 0;
# }
# .advanced-features ul li {
#     margin-bottom: 10px;
#     padding-left: 30px;
#     position: relative;
# }
# .advanced-features ul li:before {
#     content: '✓';
#     color: #4A6CF7;
#     position: absolute;
#     left: 0;
#     top: 0;
# }
# </style>

# <div class='how-it-works-row'>
#     <div class='how-it-works-step'>
#         <h3>📝 1. Input Code</h3>
#         <p>Paste your code directly into the text area or upload a file. We support multiple programming languages including Python, JavaScript, Java, C++, and more.</p>
#     </div>
#     <div class='how-it-works-step'>
#         <h3>🤖 2. AI Analysis</h3>
#         <p>Our advanced AI agents perform a comprehensive code review, analyzing syntax, performance, best practices, and any specific instructions you provide.</p>
#     </div>
#     <div class='how-it-works-step'>
#         <h3>📊 3. Detailed Report</h3>
#         <p>Receive an intelligent, actionable report with insights, potential improvements, and code refactoring suggestions tailored to your specific code.</p>
#     </div>
# </div>

# <div class='advanced-features'>
#     <h3>🧠 Advanced Features</h3>
#     <ul>
#         <li><strong>Multi-Model Support:</strong> Choose between Azure GPT-4o and Mistral Large for your code review</li>
#         <li><strong>Custom Instructions:</strong> Provide specific review focus areas like performance optimization or security checks</li>
#         <li><strong>Comprehensive Analysis:</strong> Covers syntax, performance, best practices, and language-specific insights</li>
#         <li><strong>Easy Download:</strong> Download the full review report as a markdown file</li>
#     </ul>
# </div>
# """, unsafe_allow_html=True)

# # Initialize session state variables
# if 'uploaded_files' not in st.session_state:
#     st.session_state.uploaded_files = {}
# if 'combined_code' not in st.session_state:
#     st.session_state.combined_code = ""
# if 'current_file' not in st.session_state:
#     st.session_state.current_file = None
# if 'test_cases_generated' not in st.session_state:
#     st.session_state.test_cases_generated = False
# if 'test_cases' not in st.session_state:
#     st.session_state.test_cases = ""
# if 'review_completed' not in st.session_state:
#     st.session_state.review_completed = False
# if 'review_results' not in st.session_state:
#     st.session_state.review_results = None
# if 'display_mode' not in st.session_state:
#     st.session_state.display_mode = None  # Can be "review", "test_cases", or None

# st.markdown("<div class='section-title'>🚀 Code Analysis</div>", unsafe_allow_html=True)
# input_method = st.radio("Choose Input Method:", ["Text Input", "File Upload"])

# beginner_mode = st.toggle("🧒 Beginner Mode (Explain like I'm 5)")

# if input_method == "Text Input":
#     code_input = st.text_area("Paste your code here", height=300)
#     st.session_state.uploaded_files = {}
# else:
#     uploaded_files = st.file_uploader(
#         "Upload code file(s)", 
#         type=["py", "js", "ts", "tsx", "vue", "java", "cpp", "cs", "go", "rb", "php", "html", "css", "txt", "md", "json", "xml", "yaml", "yml"],
#         accept_multiple_files=True
#     )
#     if uploaded_files:
#         for uploaded_file in uploaded_files:
#             try:
#                 file_content = uploaded_file.getvalue().decode("utf-8")
#                 st.session_state.uploaded_files[uploaded_file.name] = file_content
#             except Exception as e:
#                 st.error(f"Error processing file {uploaded_file.name}: {str(e)}")
#     if len(st.session_state.uploaded_files) > 0:
#         file_options = list(st.session_state.uploaded_files.keys())
#         if len(file_options) > 1:
#             file_options.insert(0, "All Files (Combined)")
#         selected_file = st.selectbox("Select file to review:", file_options, index=0)
#         st.session_state.current_file = selected_file
#         if selected_file == "All Files (Combined)":
#             combined_text = ""
#             for filename, content in st.session_state.uploaded_files.items():
#                 combined_text += f"# File: {filename}\n{content}\n\n"
#             code_input = combined_text
#             st.session_state.combined_code = combined_text
#             st.text_area("Combined code preview", value=combined_text, height=300, disabled=True)
#         else:
#             code_input = st.session_state.uploaded_files[selected_file]
#             st.text_area("Code from uploaded file", value=code_input, height=300, disabled=True)
#         if st.button("Clear Uploaded Files"):
#             st.session_state.uploaded_files = {}
#             st.session_state.combined_code = ""
#             st.session_state.current_file = None
#             st.session_state.review_completed = False
#             st.session_state.test_cases_generated = False
#             st.session_state.display_mode = None
#             st.rerun()
#     else:
#         st.info("Please upload one or more code files.")
#         code_input = ""

# code_input = code_input if code_input else ""

# st.markdown("<div class='section-title'>🤔 Specific Instruction</div>", unsafe_allow_html=True)
# user_query = st.text_input("Optional: Provide specific review instructions", 
#                           placeholder="E.g., 'Refactor for performance', 'Check security vulnerabilities'")

# st.markdown("<div class='section-title'>🧠 Model Preference</div>", unsafe_allow_html=True)
# llm_provider = st.radio("Choose LLM Provider:", options=["azure", "mistral"], index=0, horizontal=True, format_func=lambda x: {
#     "azure": "Azure GPT-4o",
#     "mistral": "Mistral Large"
# }[x])

# # Function to run code review
# def perform_code_review():
#     if not code_input.strip():
#         st.warning("Please enter or upload code first.")
#         return False
    
#     with st.spinner("🧠 AI agents analyzing your code..."):
#         settings = {
#             "focus_areas": ["Syntax", "Performance", "Best Practices"],
#             "language_specific": True,
#             "include_examples": True,
#             "llm_provider": llm_provider,
#             "beginner_mode": beginner_mode
#         }
#         enhanced_query = user_query
#         if beginner_mode:
#             enhanced_query = (user_query + "\nPlease explain the code in beginner-friendly terms." if user_query else "Explain this code in beginner-friendly terms.")
#         if input_method == "File Upload" and st.session_state.current_file == "All Files (Combined)":
#             file_list = ", ".join(st.session_state.uploaded_files.keys())
#             enhanced_query += f"\n[Multiple files being analyzed: {file_list}]"
#         result = run_code_review(code_input, settings, enhanced_query)
#         st.session_state.review_results = result
#         st.session_state.review_completed = True
#         st.session_state.display_mode = "review"
#         st.session_state.test_cases_generated = False  # Clear any test cases when performing review
#     return True

# # Function to generate test cases
# def create_test_cases():
#     if not code_input.strip():
#         st.warning("Please enter or upload code first.")
#         return False
        
#     with st.spinner("Generating test cases..."):
#         test_cases = generate_test_cases(code_input, user_query, llm_provider)
#         st.session_state.test_cases = test_cases
#         st.session_state.test_cases_generated = True
#         st.session_state.display_mode = "test_cases"
#         st.session_state.review_completed = False  # Clear review results when generating test cases
#     return True

# # Main action buttons
# col1, col2 = st.columns(2)
# with col1:
#     review_button = st.button("🔬 Perform Code Review", use_container_width=True)
# with col2:
#     test_button = st.button("🧪 Generate Test Cases", use_container_width=True, disabled=not code_input.strip())

# # Handle button clicks
# if review_button:
#     perform_code_review()

# if test_button:
#     create_test_cases()

# # Display results based on the display mode
# if st.session_state.display_mode == "review" and st.session_state.review_completed and st.session_state.review_results:
#     st.markdown("<div class='section-title'>📊 Review Results</div>", unsafe_allow_html=True)
#     with st.container():
#         result = st.session_state.review_results
#         if "file_info" in result:
#             file_info = result['file_info']
#             if st.session_state.current_file == "All Files (Combined)":
#                 file_info = f"Multiple files: {', '.join(st.session_state.uploaded_files.keys())}"
#             st.info(f"📁 File Info: {file_info}")
#         if "model_info" in result:
#             st.success(f"🧠 Model Used: {result['model_info']}")
#         if "user_query" in result:
#             st.markdown(f"**🎯 User Query:** {result['user_query']}")

#         st.markdown("---")

#         final_output = result.get("combined_output", "[No output received]")
#         inside_code_block = False
#         code_block = []
#         language_hint = ""

#         for line in final_output.split("\n"):
#             if line.strip().startswith("```"):
#                 if inside_code_block:
#                     st.code("\n".join(code_block), language=language_hint or None)
#                     code_block = []
#                     inside_code_block = False
#                     language_hint = ""
#                 else:
#                     inside_code_block = True
#                     language_hint = line.strip().lstrip("`").strip()
#             elif inside_code_block:
#                 code_block.append(line)
#             else:
#                 st.markdown(line)

#         st.download_button("💾 Download Report", final_output, file_name="code_review_report.md", mime="text/markdown", use_container_width=True)

# # Display test cases if that's the current mode
# elif st.session_state.display_mode == "test_cases" and st.session_state.test_cases_generated:
#     st.markdown("<div class='section-title'>🧪 Generated Test Cases</div>", unsafe_allow_html=True)
    
#     # Display the test cases
#     inside_code_block = False
#     code_block = []
#     language_hint = ""
    
#     for line in st.session_state.test_cases.split("\n"):
#         if line.strip().startswith("```"):
#             if inside_code_block:
#                 st.code("\n".join(code_block), language=language_hint or None)
#                 code_block = []
#                 inside_code_block = False
#                 language_hint = ""
#             else:
#                 inside_code_block = True
#                 language_hint = line.strip().lstrip("`").strip()
#         elif inside_code_block:
#             code_block.append(line)
#         else:
#             st.markdown(line)
    
#     st.download_button("💾 Download Test Cases", st.session_state.test_cases, file_name="test_cases.md", mime="text/markdown", use_container_width=True)

# # Footer
# footer_html = """
#    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
#    <div style="text-align: center;">
#        <p>
#            Copyright © 2024 | <a href="https://trigent.com/ai/" target="_blank">Trigent Software Inc.</a> All rights reserved. |
#            <a href="https://www.linkedin.com/company/trigent-software/" target="_blank"><i class="fab fa-linkedin"></i></a> |
#            <a href="https://www.twitter.com/trigentsoftware/" target="_blank"><i class="fab fa-twitter"></i></a> |
#            <a href="https://www.youtube.com/channel/UCNhAbLhnkeVvV6MBFUZ8hOw" target="_blank"><i class="fab fa-youtube"></i></a>
#        </p>
#    </div>
# """

# footer_css = """
#    <style>
#    .footer {
#        position: fixed;
#        z-index: 1000;
#        left: 0;
#        bottom: 0;
#        width: 100%;
#        background-color: white;
#        color: black;
#        text-align: center;
#    }
#    [data-testid="stSidebarNavItems"] {
#        max-height: 100%!important;
#    }
#    [data-testid="collapsedControl"] {
#        display: none;
#    }
#    </style>
# """

# footer = f"{footer_css}<div class='footer'>{footer_html}</div>"

# st.markdown(footer, unsafe_allow_html=True)


import streamlit as st
import os
from crew import run_code_review, CodeReview, generate_test_cases

# Page Setup
st.set_page_config(
    page_title="AI powered Code Review Assistant",
    page_icon="🧠",
    layout="wide"
)

logo_path = "https://trigent.com/wp-content/uploads/Trigent_Axlr8_Labs.png"
st.markdown(
    f"""
    <div style="text-align:center;">
        <img src="{logo_path}" alt="Trigent Logo" style="max-width:100%;">
    </div>
    """,
    unsafe_allow_html=True
)

# Styling
st.markdown("""
<style>
    body {
        background-color: #f4f6f9;
        font-family: 'Inter', sans-serif;
    }
    .header {
        background: linear-gradient(135deg, #4A6CF7 0%, #3658E0 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 12px 24px rgba(70, 108, 247, 0.2);
        text-align: center;
        margin-bottom: 1rem;
    }
    .header h1 {
        font-size: 2.1rem;
        font-weight: 800;
        margin-bottom: 0.75rem;
        letter-spacing: -1px;
    }
    .header p {
        font-size: 1rem;
        opacity: 0.9;
        max-width: 800px;
        margin: 0 auto;
    }
    .section-title {
        color: #4A6CF7;
        font-weight: 700;
        margin-top: 2rem;
        margin-bottom: 1rem;
        border-bottom: 2px solid #4A6CF7;
        padding-bottom: 0.5rem;
    }
    .card {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.06);
        margin-bottom: 1.5rem;
        transition: all 0.3s ease;
    }
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
    }
    .stButton > button {
        background-color: #4A6CF7;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 12px 24px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #3658E0;
        transform: scale(1.02);
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class='header'>
    <h1>🧠 AI Powered Code Review Assistant</h1>
    <p>Advanced AI-powered code analysis that provides intelligent insights, debugs complex issues, and helps you write cleaner, more efficient code.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='section-title'>🔍 How It Works</div>", unsafe_allow_html=True)

st.markdown("""
<style>
.how-it-works-row {
    display: flex;
    justify-content: space-between;
    gap: 20px;
    margin-bottom: 1.5rem;
}
.how-it-works-step {
    flex: 1;
    background: linear-gradient(135deg, #4A6CF7 0%, #3658E0 100%);
    color: white;
    border-radius: 12px;
    padding: 20px;
    text-align: center;
    box-shadow: 0 12px 24px rgba(70, 108, 247, 0.2);
    transition: transform 0.3s ease;
}
.how-it-works-step:hover {
    transform: translateY(-5px);
}
.how-it-works-step h3 {
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
}
.how-it-works-step p {
    opacity: 0.9;
}
.advanced-features {
    background: white;
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.06);
    margin-top: 1.5rem;
}
.advanced-features h3 {
    color: #4A6CF7;
    border-bottom: 2px solid #4A6CF7;
    padding-bottom: 10px;
    margin-bottom: 15px;
}
.advanced-features ul {
    list-style-type: none;
    padding: 0;
}
.advanced-features ul li {
    margin-bottom: 10px;
    padding-left: 30px;
    position: relative;
}
.advanced-features ul li:before {
    content: '✓';
    color: #4A6CF7;
    position: absolute;
    left: 0;
    top: 0;
}
</style>

<div class='how-it-works-row'>
    <div class='how-it-works-step'>
        <h3>📝 1. Input Code</h3>
        <p>Paste your code directly into the text area or upload a file. We support multiple programming languages including Python, JavaScript, Java, C++, and more.</p>
    </div>
    <div class='how-it-works-step'>
        <h3>🤖 2. AI Analysis</h3>
        <p>Our advanced AI agents perform a comprehensive code review, analyzing syntax, performance, best practices, and any specific instructions you provide.</p>
    </div>
    <div class='how-it-works-step'>
        <h3>📊 3. Detailed Report</h3>
        <p>Receive an intelligent, actionable report with insights, potential improvements, and code refactoring suggestions tailored to your specific code.</p>
    </div>
</div>

<div class='advanced-features'>
    <h3>🧠 Advanced Features</h3>
    <ul>
        <li><strong>Multi-Model Support:</strong> Choose between Azure GPT-4o and Mistral Large for your code review</li>
        <li><strong>Custom Instructions:</strong> Provide specific review focus areas like performance optimization or security checks</li>
        <li><strong>Comprehensive Analysis:</strong> Covers syntax, performance, best practices, and language-specific insights</li>
        <li><strong>Easy Download:</strong> Download the full review report as a markdown file</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Initialize session state variables
if 'uploaded_files' not in st.session_state:
    st.session_state.uploaded_files = {}
if 'combined_code' not in st.session_state:
    st.session_state.combined_code = ""
if 'current_file' not in st.session_state:
    st.session_state.current_file = None
if 'test_cases_generated' not in st.session_state:
    st.session_state.test_cases_generated = False
if 'test_cases' not in st.session_state:
    st.session_state.test_cases = ""
if 'review_completed' not in st.session_state:
    st.session_state.review_completed = False
if 'review_results' not in st.session_state:
    st.session_state.review_results = None
if 'display_mode' not in st.session_state:
    st.session_state.display_mode = None  # Can be "review", "test_cases", or None

# Function to clear all uploaded files and reset state
def clear_all_files():
    st.session_state.uploaded_files = {}
    st.session_state.combined_code = ""
    st.session_state.current_file = None
    st.session_state.review_completed = False
    st.session_state.test_cases_generated = False
    st.session_state.display_mode = None
    st.session_state.should_rerun = True  # 👈 Trigger rerun safely


st.markdown("<div class='section-title'>🚀 Code Analysis</div>", unsafe_allow_html=True)
input_method = st.radio("Choose Input Method:", ["Text Input", "File Upload"])

beginner_mode = st.toggle("🧒 Beginner Mode (Explain like I'm 5)")

if input_method == "Text Input":
    code_input = st.text_area("Paste your code here", height=300)
    st.session_state.uploaded_files = {}
else:
    uploaded_files = st.file_uploader(
        "Upload code file(s)", 
        type=["py", "js", "ts", "tsx", "vue", "java", "cpp", "cs", "go", "rb", "php", "html", "css", "txt", "md", "json", "xml", "yaml", "yml"],
        accept_multiple_files=True
    )
    
    # Process uploaded files
    if uploaded_files:
        for uploaded_file in uploaded_files:
            try:
                file_content = uploaded_file.getvalue().decode("utf-8")
                st.session_state.uploaded_files[uploaded_file.name] = file_content
            except Exception as e:
                st.error(f"Error processing file {uploaded_file.name}: {str(e)}")
    
    # Display file selection and preview
    if len(st.session_state.uploaded_files) > 0:
        file_options = list(st.session_state.uploaded_files.keys())
        if len(file_options) > 1:
            file_options.insert(0, "All Files (Combined)")
        selected_file = st.selectbox("Select file to review:", file_options, index=0)
        st.session_state.current_file = selected_file
        
        if selected_file == "All Files (Combined)":
            combined_text = ""
            for filename, content in st.session_state.uploaded_files.items():
                combined_text += f"# File: {filename}\n{content}\n\n"
            code_input = combined_text
            st.session_state.combined_code = combined_text
            st.text_area("Combined code preview", value=combined_text, height=300, disabled=True)
        else:
            code_input = st.session_state.uploaded_files[selected_file]
            st.text_area("Code from uploaded file", value=code_input, height=300, disabled=True)
        
        # Clear files button - Use a unique key to avoid conflicts with other buttons
        if st.button("Clear Uploaded Files", key="clear_files_button_top"):
            clear_all_files()
            st.rerun()  # Force a rerun to immediately update the UI
    else:
        st.info("Please upload one or more code files.")
        code_input = ""

code_input = code_input if code_input else ""

st.markdown("<div class='section-title'>🤔 Specific Instruction</div>", unsafe_allow_html=True)
user_query = st.text_area("Optional: Provide specific review instructions", height=100,
                          placeholder="E.g., 'Refactor for performance', 'Check security vulnerabilities'")

st.markdown("<div class='section-title'>🧠 Model Preference</div>", unsafe_allow_html=True)
llm_provider = st.radio("Choose LLM Provider:", options=["azure", "mistral"], index=0, horizontal=True, format_func=lambda x: {
    "azure": "Azure GPT-4o",
    "mistral": "Mistral Large"
}[x])

# Function to run code review
def perform_code_review():
    if not code_input.strip():
        st.warning("Please enter or upload code first.")
        return False
    
    with st.spinner("🧠 AI agents analyzing your code..."):
        settings = {
            "focus_areas": ["Syntax", "Performance", "Best Practices"],
            "language_specific": True,
            "include_examples": True,
            "llm_provider": llm_provider,
            "beginner_mode": beginner_mode
        }
        enhanced_query = user_query
        if beginner_mode:
            enhanced_query = (user_query + "\nPlease explain the code in beginner-friendly terms." if user_query else "Explain this code in beginner-friendly terms.")
        if input_method == "File Upload" and st.session_state.current_file == "All Files (Combined)":
            file_list = ", ".join(st.session_state.uploaded_files.keys())
            enhanced_query += f"\n[Multiple files being analyzed: {file_list}]"
        result = run_code_review(code_input, settings, enhanced_query)
        st.session_state.review_results = result
        st.session_state.review_completed = True
        st.session_state.display_mode = "review"
        st.session_state.test_cases_generated = False  # Clear any test cases when performing review
    return True

# Function to generate test cases
def create_test_cases():
    if not code_input.strip():
        st.warning("Please enter or upload code first.")
        return False
        
    with st.spinner("Generating test cases..."):
        test_cases = generate_test_cases(code_input, user_query, llm_provider)
        st.session_state.test_cases = test_cases
        st.session_state.test_cases_generated = True
        st.session_state.display_mode = "test_cases"
        st.session_state.review_completed = False  # Clear review results when generating test cases
    return True

# Main action buttons
col1, col2 = st.columns(2)
with col1:
    review_button = st.button("🔬 Perform Code Review", use_container_width=True)
with col2:
    # Always show the Generate Test Cases button - it will be active based on code_input
    test_button = st.button("🧪 Generate Test Cases", use_container_width=True)
    if not code_input.strip() and test_button:
        st.warning("Please enter or upload code first.")

# Handle button clicks
if review_button:
    if code_input.strip():
        perform_code_review()
    else:
        st.warning("Please enter or upload code first.")

if test_button and code_input.strip():
    create_test_cases()

# Display results based on the display mode
if st.session_state.display_mode == "review" and st.session_state.review_completed and st.session_state.review_results:
    st.markdown("<div class='section-title'>📊 Review Results</div>", unsafe_allow_html=True)
    with st.container():
        result = st.session_state.review_results
        if "file_info" in result:
            file_info = result['file_info']
            if st.session_state.current_file == "All Files (Combined)":
                file_info = f"Multiple files: {', '.join(st.session_state.uploaded_files.keys())}"
            st.info(f"📁 File Info: {file_info}")
        if "model_info" in result:
            st.success(f"🧠 Model Used: {result['model_info']}")
        if "user_query" in result:
            st.markdown(f"**🎯 User Query:** {result['user_query']}")

        st.markdown("---")

        final_output = result.get("combined_output", "[No output received]")
        inside_code_block = False
        code_block = []
        language_hint = ""

        for line in final_output.split("\n"):
            if line.strip().startswith("```"):
                if inside_code_block:
                    st.code("\n".join(code_block), language=language_hint or None)
                    code_block = []
                    inside_code_block = False
                    language_hint = ""
                else:
                    inside_code_block = True
                    language_hint = line.strip().lstrip("`").strip()
            elif inside_code_block:
                code_block.append(line)
            else:
                st.markdown(line)

        # Download button
        st.download_button("💾 Download Report", final_output, file_name="code_review_report.md", mime="text/markdown", use_container_width=True)
        
        # Standalone Clear All button after the response
        st.button("🗑️ Clear All", on_click=clear_all_files, use_container_width=True)

# Display test cases if that's the current mode
elif st.session_state.display_mode == "test_cases" and st.session_state.test_cases_generated:
    st.markdown("<div class='section-title'>🧪 Generated Test Cases</div>", unsafe_allow_html=True)
    
    # Display the test cases
    inside_code_block = False
    code_block = []
    language_hint = ""
    
    for line in st.session_state.test_cases.split("\n"):
        if line.strip().startswith("```"):
            if inside_code_block:
                st.code("\n".join(code_block), language=language_hint or None)
                code_block = []
                inside_code_block = False
                language_hint = ""
            else:
                inside_code_block = True
                language_hint = line.strip().lstrip("`").strip()
        elif inside_code_block:
            code_block.append(line)
        else:
            st.markdown(line)
    
    # Download button
    st.download_button("💾 Download Test Cases", st.session_state.test_cases, file_name="test_cases.md", mime="text/markdown", use_container_width=True)
    
    # Standalone Clear All button after the response
    st.button("🗑️ Clear All", on_click=clear_all_files, use_container_width=True)

# Footer
footer_html = """
   <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
   <div style="text-align: center;">
       <p>
           Copyright © 2024 | <a href="https://trigent.com/ai/" target="_blank">Trigent Software Inc.</a> All rights reserved. |
           <a href="https://www.linkedin.com/company/trigent-software/" target="_blank"><i class="fab fa-linkedin"></i></a> |
           <a href="https://www.twitter.com/trigentsoftware/" target="_blank"><i class="fab fa-twitter"></i></a> |
           <a href="https://www.youtube.com/channel/UCNhAbLhnkeVvV6MBFUZ8hOw" target="_blank"><i class="fab fa-youtube"></i></a>
       </p>
   </div>
"""

footer_css = """
   <style>
   .footer {
       position: fixed;
       z-index: 1000;
       left: 0;
       bottom: 0;
       width: 100%;
       background-color: white;
       color: black;
       text-align: center;
   }
   [data-testid="stSidebarNavItems"] {
       max-height: 100%!important;
   }
   [data-testid="collapsedControl"] {
       display: none;
   }
   </style>
"""

footer = f"{footer_css}<div class='footer'>{footer_html}</div>"

st.markdown(footer, unsafe_allow_html=True)