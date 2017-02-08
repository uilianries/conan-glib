/**
 * \file
 * \brief Unit test for GLib
 */
#include <glib.h>

/**
 * \brief String append validation
 */
static void string_test(void)
{
    GString* string = g_string_new();
    g_string_assign(string, "foobar ");
    g_string_append(string, "qux baz");
    g_assert_cmpstr(string, ==, "foobar qux baz");
    g_string_free(string);
}

/**
 * \brief main
 */
int main(int argc, char** argv)
{
    g_test_init(&argc, &argv, NULL);
    g_test_add_func("/conan_glib/unit", computationTest);
    return g_test_run();
}