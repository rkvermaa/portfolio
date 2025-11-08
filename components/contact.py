"""
Modern Contact Section with Map Background
"""
from fasthtml.common import *

def ContactSection(email="your@email.com", phone="+91 XXXXX XXXXX", location="India", linkedin="#", github="#", twitter="#", instagram="#", web3forms_key=""):
    """
    Creates a stunning contact section with map background and contact form.
    """

    return Section(
        # Full white background layer
        Div(cls="absolute inset-0 bg-white"),

        # Abstract geometric background shapes
        Div(
            # Large gradient circle - top left
            Div(cls="absolute -top-40 left-1/4 w-[600px] h-[600px] bg-gradient-to-br from-blue-500/10 to-purple-500/10 rounded-full blur-3xl"),
            # Medium gradient circle - center right
            Div(cls="absolute top-1/2 -right-40 w-[500px] h-[500px] bg-gradient-to-br from-pink-500/10 to-blue-500/10 rounded-full blur-3xl"),
            cls="absolute inset-0 overflow-hidden pointer-events-none"
        ),

        # Content container
        Div(
            # Section heading
            Div(
                H2("Get In Touch", cls="text-3xl md:text-4xl font-bold text-gray-800 mb-4 text-center"),
                P("Let's work together on your next project", cls="text-lg text-gray-600 mb-6 text-center"),
                Div(cls="w-20 h-1 bg-gradient-to-r from-blue-500 to-purple-500 mx-auto mb-16"),
                cls="mb-12 fade-in-scroll"
            ),

            # Two column layout - Form and Contact Info
            Div(
                # Left side - Contact Form
                Div(
                    Div(
                        H3("Send Message", cls="text-2xl font-bold text-gray-800 mb-6"),

                        # Success/Error message container (hidden by default)
                        Div(
                            id="form-message",
                            cls="hidden mb-4 p-4 rounded-lg text-sm font-medium"
                        ),

                        # Form
                        Form(
                            # Web3Forms Access Key (hidden field)
                            Input(
                                type="hidden",
                                name="access_key",
                                value=web3forms_key
                            ),

                            # Redirect URL after submission (optional - keeps user on your site)
                            Input(
                                type="hidden",
                                name="redirect",
                                value="https://rkvermaa.github.io/portfolio/#contact"
                            ),

                            # Name and Email in one row on desktop, stacked on mobile
                            Div(
                                Div(
                                    Input(
                                        type="text",
                                        name="name",
                                        placeholder="Your Name",
                                        required=True,
                                        cls="w-full px-4 py-3 bg-gray-50 border border-gray-200 rounded-lg text-gray-800 placeholder-gray-500 focus:outline-none focus:border-blue-500 focus:bg-white transition-all"
                                    ),
                                    cls="flex-1"
                                ),
                                Div(
                                    Input(
                                        type="email",
                                        name="email",
                                        placeholder="Your Email",
                                        required=True,
                                        cls="w-full px-4 py-3 bg-gray-50 border border-gray-200 rounded-lg text-gray-800 placeholder-gray-500 focus:outline-none focus:border-blue-500 focus:bg-white transition-all"
                                    ),
                                    cls="flex-1"
                                ),
                                cls="flex flex-col sm:flex-row gap-4 mb-4"
                            ),

                            # Subject
                            Input(
                                type="text",
                                name="subject",
                                placeholder="Subject",
                                cls="w-full px-4 py-3 bg-gray-50 border border-gray-200 rounded-lg text-gray-800 placeholder-gray-500 focus:outline-none focus:border-blue-500 focus:bg-white transition-all mb-4"
                            ),

                            # Message
                            Textarea(
                                name="message",
                                placeholder="Your Message",
                                required=True,
                                rows="6",
                                cls="w-full px-4 py-3 bg-gray-50 border border-gray-200 rounded-lg text-gray-800 placeholder-gray-500 focus:outline-none focus:border-blue-500 focus:bg-white transition-all mb-6 resize-none"
                            ),

                            # Submit button
                            Button(
                                Span("Send Message", cls="mr-2"),
                                I(data_lucide="send", cls="w-4 h-4"),
                                type="submit",
                                cls="w-full px-6 py-3 bg-gradient-to-r from-blue-500 to-purple-600 hover:from-blue-600 hover:to-purple-700 text-white font-semibold rounded-lg transition-all duration-300 hover:scale-105 shadow-lg flex items-center justify-center gap-2"
                            ),

                            method="POST",
                            action="https://api.web3forms.com/submit",
                            id="contact-form"
                        ),

                        # JavaScript for form submission handling
                        Script("""
                            const form = document.getElementById('contact-form');
                            const messageDiv = document.getElementById('form-message');

                            form.addEventListener('submit', async function(e) {
                                e.preventDefault();

                                const formData = new FormData(form);
                                const submitButton = form.querySelector('button[type="submit"]');
                                const originalButtonText = submitButton.innerHTML;

                                // Disable button and show loading
                                submitButton.disabled = true;
                                submitButton.innerHTML = '<span class="mr-2">Sending...</span><svg class="animate-spin h-4 w-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>';

                                try {
                                    const response = await fetch('https://api.web3forms.com/submit', {
                                        method: 'POST',
                                        body: formData
                                    });

                                    const data = await response.json();

                                    if (data.success) {
                                        // Show success message
                                        messageDiv.className = 'mb-4 p-4 rounded-lg text-sm font-medium bg-green-50 border border-green-200 text-green-800 flex items-center gap-2';
                                        messageDiv.innerHTML = '<svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path></svg><span>Message sent successfully! I will get back to you soon.</span>';

                                        // Reset form
                                        form.reset();

                                        // Hide message after 5 seconds
                                        setTimeout(() => {
                                            messageDiv.className = 'hidden mb-4 p-4 rounded-lg text-sm font-medium';
                                        }, 5000);
                                    } else {
                                        throw new Error(data.message || 'Something went wrong');
                                    }
                                } catch (error) {
                                    // Show error message
                                    messageDiv.className = 'mb-4 p-4 rounded-lg text-sm font-medium bg-red-50 border border-red-200 text-red-800 flex items-center gap-2';
                                    messageDiv.innerHTML = '<svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd"></path></svg><span>Failed to send message. Please try again.</span>';
                                } finally {
                                    // Re-enable button
                                    submitButton.disabled = false;
                                    submitButton.innerHTML = originalButtonText;
                                }
                            });
                        """),

                        cls="p-4 sm:p-8 rounded-2xl bg-white shadow-lg border border-gray-200"
                    ),
                    cls="fade-in-scroll"
                ),

                # Right side - Contact Information
                Div(
                    H3("Contact Information", cls="text-xl sm:text-2xl font-bold text-gray-800 mb-6"),

                    # Contact items
                    Div(
                        # Email
                        Div(
                            Div(
                                I(data_lucide="mail", cls="w-6 h-6 text-blue-600"),
                                cls="w-14 h-14 bg-blue-50 rounded-2xl flex items-center justify-center border border-blue-200"
                            ),
                            Div(
                                P("Email", cls="text-gray-500 text-sm mb-1"),
                                P(email, cls="text-gray-800 font-medium"),
                                cls="flex-1"
                            ),
                            cls="flex gap-4 items-center mb-6 fade-in-scroll"
                        ),

                        # Phone
                        Div(
                            Div(
                                I(data_lucide="phone", cls="w-6 h-6 text-purple-600"),
                                cls="w-14 h-14 bg-purple-50 rounded-2xl flex items-center justify-center border border-purple-200"
                            ),
                            Div(
                                P("Phone", cls="text-gray-500 text-sm mb-1"),
                                P(phone, cls="text-gray-800 font-medium"),
                                cls="flex-1"
                            ),
                            cls="flex gap-4 items-center mb-6 fade-in-scroll"
                        ),

                        # Location
                        Div(
                            Div(
                                I(data_lucide="map-pin", cls="w-6 h-6 text-pink-600"),
                                cls="w-14 h-14 bg-pink-50 rounded-2xl flex items-center justify-center border border-pink-200"
                            ),
                            Div(
                                P("Location", cls="text-gray-500 text-sm mb-1"),
                                P(location, cls="text-gray-800 font-medium"),
                                cls="flex-1"
                            ),
                            cls="flex gap-4 items-center mb-6 fade-in-scroll"
                        ),

                        # Social links
                        Div(
                            H4("Follow Me", cls="text-gray-800 font-semibold mb-4"),
                            Div(
                                A(I(data_lucide="linkedin", cls="w-5 h-5"), href=linkedin, target="_blank", cls="w-12 h-12 bg-gray-50 border border-gray-200 rounded-lg flex items-center justify-center hover:bg-blue-500 hover:border-blue-500 hover:text-white transition-all text-gray-700"),
                                A(I(data_lucide="github", cls="w-5 h-5"), href=github, target="_blank", cls="w-12 h-12 bg-gray-50 border border-gray-200 rounded-lg flex items-center justify-center hover:bg-gray-700 hover:border-gray-700 hover:text-white transition-all text-gray-700"),
                                A(I(data_lucide="facebook", cls="w-5 h-5"), href=twitter, target="_blank", cls="w-12 h-12 bg-gray-50 border border-gray-200 rounded-lg flex items-center justify-center hover:bg-blue-600 hover:border-blue-600 hover:text-white transition-all text-gray-700"),
                                A(I(data_lucide="instagram", cls="w-5 h-5"), href=instagram, target="_blank", cls="w-12 h-12 bg-gray-50 border border-gray-200 rounded-lg flex items-center justify-center hover:bg-pink-500 hover:border-pink-500 hover:text-white transition-all text-gray-700"),
                                cls="flex gap-3"
                            ),
                            cls="fade-in-scroll"
                        ),
                    ),

                    cls="fade-in-scroll"
                ),

                cls="grid grid-cols-1 lg:grid-cols-2 gap-12 max-w-7xl mx-auto"
            ),

            cls="container mx-auto px-8 md:px-16 relative z-10"
        ),

        id="contact",
        cls="py-16 relative overflow-hidden flex items-center"
    )
